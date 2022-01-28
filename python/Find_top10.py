#!/usr/bin/python
#
#
#

import os
import sys
import string
import gzip
import math

MIN_PYTHON=(3,5)
if sys.version_info < MIN_PYTHON:
    sys.exit("Python %s.%s or later is required.\n" % MIN_PYTHON)

THRESHOLD=2

def read_Matrix(matrix_file):
    scoring_matrix=dict()
    with open(matrix_file,"rb") as f:
        count=0
        while True:
            line=f.readline()
            if count==0:
                count+=1
                continue
            if not line:
                break
            line=line.decode("utf-8").rstrip().split()
            scoring_matrix[line[0]]=line[1:]
            count+=1
    return scoring_matrix
    
def score_Seq(seq,matrix):
    values=[float(matrix[nt][i]) for i,nt in enumerate(seq)]
    #ARGGWISLYYDSSGYPNFDY
    #linear sum of the inverse of the score in the matrix
    score=0.0
    for i,v in enumerate(values):
        if v<=THRESHOLD:
            v=v-1000000
        if i==7:#case to not score the 8th position (python starts at 0)
            continue
        elif math.isclose(float(v),0.0):
            #score+=1.0/0.0001 #adaptation for zero
            score+=float(v)
        else:
            #score+=1.0/float(v)
            score+=float(v)
    #print("{}:{:.4f}".format(seq,score))
    return score

def processGZfile(filename,matrix):
    with open(filename.replace(".gz",".score"),'w') as out:
        with gzip.open(filename, 'rb') as f:
            while True:
                line=f.readline()
                if not line:
                    break
                seq,Dvalue=line.rstrip().split()
                score=score_Seq(seq.decode("utf-8")[1:21],matrix)
                out.write("{}\t{:.4f}\n".format(seq[1:21],score))

def print_list(outfile,s_list):
    #ss_list=sorted(s_list,key = lambda x: float(x[1]))

    with open(outfile,"w") as out:
        [out.write("{}\t{:.4f}\n".format(tup[0],tup[1])) for tup in set(s_list)]
    os.system("sort -k2 -r -n {} > tmp".format(outfile))
    os.system("mv tmp {}".format(outfile))
def processTXTfile(filename,matrix):
    seq_list=[]
    L_seq_list=[]
    ALV_seq_list=[]
    max_number=100
    with open(filename, "r") as f:
        while True:
            line=f.readline()
            if not line:
                break
            try:
                seq=line.rstrip().split()[0]
            except:
                print(line)
                exit()
                
            if len(seq)==20:
                score=score_Seq(seq,matrix)
                if seq[7]=="L":
                    L_seq_list.append((seq,float(score)))
                    if len(set(L_seq_list))>max_number:
                        lowValue=min(L_seq_list,key=lambda t: t[1])
                        L_seq_list.remove(lowValue)
                    
                if seq[7]=="L" or seq[7]=="A" or seq[7]=="V":
                    ALV_seq_list.append((seq,score))
                    if len(set(ALV_seq_list))>max_number:
                        lowValue=min(ALV_seq_list,key=lambda t: t[1])
                        ALV_seq_list.remove(lowValue)
                    
                seq_list.append((seq,score))
                if len(set(seq_list))>max_number:
                    lowValue=min(seq_list,key=lambda t: t[1])
                    seq_list.remove(lowValue)
                    
    #with open(filename+".{}.top100".format(THRESHOLD),"w") as out:
    #    [out.write("{}\t{:.4f}\n".format(tup[0],tup[1])) for tup in set(seq_list)]
    #with open(filename+".{}.L.top100".format(THRESHOLD),"w") as out:
    #    [out.write("{}\t{:.4f}\n".format(tup[0],tup[1])) for tup in set(L_seq_list)]
    #with open(filename+".{}.ALV.top100".format(THRESHOLD),"w") as out:
    #    [out.write("{}\t{:.4f}\n".format(tup[0],tup[1])) for tup in set(ALV_seq_list)]
    print_list(filename+".{}.top{}".format(THRESHOLD,max_number),seq_list)
    print_list(filename+".{}.L.top{}".format(THRESHOLD,max_number),L_seq_list)
    print_list(filename+".{}.ALV.top{}".format(THRESHOLD,max_number),ALV_seq_list)
                
def main(filename,matrixfile):
    count=0
    matrix=read_Matrix(matrixfile)
    if filename[-2:]=="gz":
        processGZfile(filename,matrix)
    else:
        processTXTfile(filename,matrix)


if __name__=="__main__":
    #argument 1 is filename
    #argument 2 is the scoring matrix
    #argument 3 is the threshold value
    THRESHOLD=float(sys.argv[3])
    main(sys.argv[1],sys.argv[2])

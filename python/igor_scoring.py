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

def processTXTfile(filename,matrix):
    with open(filename+".score",'w') as out:
        with open(filename, "r") as f:
            while True:
                line=f.readline()
                if not line:
                    break
                seq=line.rstrip()
                #print("{}-length:{}".format(seq,len(seq)))
                if len(seq)==20:
                    score=score_Seq(seq,matrix)
                    out.write("{}\t{:.4f}\n".format(seq,score))

                
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
    main(sys.argv[1],sys.argv[2])

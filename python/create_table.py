#!/usr/bin/python


#libraries
import xlrd, re
import glob
import os
import string
import sys,math
import numpy,scipy

def read_score_matrix(matrix_file):
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

def score_Seq(seq,matrix,cutoff):
    values=[float(matrix[nt][i]) for i,nt in enumerate(seq)]
    #ARGGWISLYYDSSGYPNFDY
    #linear sum of the inverse of the score in the matrix
    distance=0
    for i,v in enumerate(values):
        #if i==7:#case to ignore 8th position
        #    continue
        if v<cutoff:
            distance=distance+1

    return distance


def main(matrix_file,infile,cutoff):
    score_matrix=read_score_matrix(matrix_file)
    seq_length=len(score_matrix['A'])
    dist_counts=dict()
    for i in range(seq_length+1):
        dist_counts[i]=0
    with open(infile,"r") as f:
        counter=0
        while True:
            line=f.readline()
            if len(line)<2:
                break
            counter=counter+1
            line=line.rstrip().split()
            if len(line)>1:
                seq=line[1]
            else:
                continue
            if 'X' in seq:
                continue
                
            if len(seq)==seq_length:
                dist=score_Seq(seq,score_matrix,float(cutoff))
                #print("{}-{}-{}".format(len(seq),seq_length,dist))
                dist_counts[dist]=dist_counts[dist]+1

                #input('e')
            else:
                continue
    #for key in dist_counts.keys():
    #    print("{} - {}".format(key,dist_counts[key]))
    #print("counter: {}".format(counter))
    percent=float(dist_counts[10])/float(counter)

    #print("{}".format(round(float(counter)/float(dist_counts[10]))))
    outstr=[infile.replace(".aa","")]
    for i in range(seq_length+1):
        if dist_counts[i]==0:
            outstr.append("NA")
        else:
            outstr.append("1 in {}".format(round(float(counter)/float(dist_counts[i]))))
    print("\t".join(outstr))
    return


if __name__=="__main__":
    main(sys.argv[1],sys.argv[2],sys.argv[3])

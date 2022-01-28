#!/usr/bin/python
#
#
#

import os
import sys
import string
import gzip
import math
import numpy

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
    score=[]
    for i,v in enumerate(values):
        if v<=THRESHOLD:
            v=v-1000000
        if i==7:#case to not score the 8th position (python starts at 0)
            score.append(0)
            continue
        elif math.isclose(float(v),0.0):
            #score+=1.0/0.0001 #adaptation for zero
            score.append(float(v))
        else:
            #score+=1.0/float(v)
            score.append(float(v))
    #print("{}:{:.4f}".format(seq,score))
    return score



    
def processTXTfile(seq,matrix):
    seq_list=[]
    L_seq_list=[]
    ALV_seq_list=[]
    max_number=100
    if len(seq)==20:
        score=score_Seq(seq,matrix)
    else:
        print("can not score seq:{}\ncheck length".format(seq))
        exit()
    print(",".join([x for x in seq]))
    print(score)
    print(numpy.sum(score))
                
                
def main(seq,matrixfile):
    count=0
    matrix=read_Matrix(matrixfile)
    processTXTfile(seq,matrix)


if __name__=="__main__":
    #argument 1 is filename
    #argument 2 is the scoring matrix
    #argument 3 is the threshold value
    THRESHOLD=float(sys.argv[3])
    main(sys.argv[1],sys.argv[2])

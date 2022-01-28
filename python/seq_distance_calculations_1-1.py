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
    all_dist=[]
    #print(seq)
    for cutoff in [x/5.0 for x in range(-5,6)]:
        dist=20
        for i,nt in enumerate(seq):
            if float(matrix[nt][i])>float(cutoff):
                dist-=1
        all_dist.append(dist)
    #print(all_dist)    
    #input('e')
    #0 -> -6
    distance="\t".join(["{}".format(i) for i in all_dist])
    return distance

def processGZfile(filename,matrix):
    with open(filename.replace(".gz",".dist"),'w') as out:
        with gzip.open(filename, 'rb') as f:
            while True:
                line=f.readline()
                if not line:
                    break
                seq,Dvalue=line.rstrip().split()
                score=score_Seq(seq.decode("utf-8")[1:21],matrix)
                out.write("{}\t{}\n".format(seq.decode("utf-8"),score))

def processTXTfile(filename,matrix):
    with open(filename+".dist",'w') as out:
        with open(filename, "r") as f:
            while True:
                line=f.readline()
                if not line:
                    break
                seq=line.rstrip()
                #print("{}-length:{}".format(seq,len(seq)))
                if len(seq)==20:
                    score=score_Seq(seq,matrix)
                    out.write("{}\t{}\n".format(seq,score))

                
def main(filename,matrixfile):
    count=0
    matrix=read_Matrix(matrixfile)
    if filename[-2:]=="gz":
        processGZfile(filename,matrix)
    else:
        processTXTfile(filename,matrix)
        
if __name__=="__main__":
    main(sys.argv[1],sys.argv[2])

#!/usr/bin/python3

#libraries
import xlrd, re
import glob
import os
import string
import sys
import numpy,scipy
from collections import deque

def read_table(intable,cdr3len):
    posDict=dict()
    for i in range(cdr3len):
        posDict[str(i)]=[]
    with open(intable,'r') as tablefile:
        while True:
            line=tablefile.readline().rstrip()
            if len(line)<2:
                break
            for i,AA in enumerate(line.split("\t")):
                if AA=="":
                    continue
                posDict[str(i)].append(AA)
    return posDict

def write_seqs(seqs,outfasta):
    with open(outfasta,'w') as outfile:
        for i,seq in enumerate(seqs):
            outfile.write(">seq_{}\n".format(i))
            outfile.write("".join(seq)+"\n")

def genSeqs(AAdict):
    uniq_counts=[]
    print(AAdict.keys())
    for values in AAdict.values():
        uniq_counts.append(len(values))
    #uniq_counts=[x for x in set(uniq_counts)]
    seq_counts=numpy.product([x for x in set(uniq_counts)])

    #print(seq_counts)
    #seq_counts=100
    #print(uniq_counts)
    #print(seq_counts/uniq_counts[1])
    #mod is 0 or 1 - fully divisible is 0
    seqs=[[] for x in range(seq_counts)]
    for i,count in enumerate(uniq_counts):
        values=deque(AAdict[str(i)])
        for seqNumb in range(seq_counts):
            #print("{} --- {}".format(seqNumb,values[0]))
            seqs[seqNumb].append(values[0])
            values.rotate(-1)
        #print(seqs)
        #input('e')
    #print(seqs)
    #input('e')
    return seqs

    
def main(intable,outfasta):
    cdr3len=0
    with open(intable,'r') as tablefile:
        line=tablefile.readline().rstrip()
    cdr3len=len(line.rstrip().split())
    AAdict=read_table(intable,cdr3len)
    seqs=genSeqs(AAdict)
    write_seqs(seqs,outfasta)
    return

if __name__=="__main__":
    main(sys.argv[1],sys.argv[2])

#!/usr/bin/python

#libraries
import xlrd, re
import glob
import os
import sys
import numpy

class Seq():
    def __init__(self,name,seq):
        self.name=name
        self.seq=seq
        self.IGHD=""
        self.IGHJ=""
        self.IGHV=""
    def add_dgene(self,dgene):
        self.IGHD=dgene
    def add_cdr3(self,cdr3):
        self.cdr3AA=cdr3

    def get_stats(self,cdr_length_target,dGene_AA):
        self.foundD=0
        self.correctLength=0
        self.Dgene_ID=0
        self.Dgene_position=0
        self.len_D_pos=0
        self.functional=0
        if dGene_AA in self.cdr3AA:
            self.foundD=1
        if len(self.cdr3AA)==20:
            self.correctLength=1           
        if "IGHD3-22" in self.IGHD:
            self.Dgene_ID=1
        if len(self.cdr3AA)>=12:
            if dGene_AA==self.cdr3AA[9:13]:
                self.Dgene_position=1
                if self.correctLength==1:
                    self.len_D_pos=1
                    if "*" not in self.cdr3AA:
                        self.functional=1
        return

def main(fastafile,resultsname="briney_results.txt"):
    seqs=[]
    all_foundD=0
    all_correctLength=0
    all_Dgene_ID=0
    all_Dgene_position=0
    all_len_D_pos=0
    all_functional=0
    with open(resultsname,'a') as outfile:
        with open(fastafile,'r') as seqfile:
            idpos=-1
            cdr3_aa_pos=-1
            seq_pos=-1
            dgene_pos=-1
            for line in seqfile:
                if "seq_id" in line:
                    headers=line.rstrip().split(',')
                    try:#idpos
                        idpos=headers.index('seq_id')
                    except:
                        idpos=-1
                    try:#cdr3_aa
                        cdr3_aa_pos=headers.index('cdr3_aa')
                    except:
                        cdr3_aa_pos=-1
                    try:#seq_pos
                        seq_pos=headers.index('raw_input')
                    except:
                        seq_pos=-1
                    try:
                        dgene_pos=headers.index("d_gene")
                    except:
                        dgene_pos=-1
                else:
                    data=line.rstrip().split(',')
                    temp=Seq("","")
                    try:
                        if idpos!=-1:
                            temp.name=data[idpos]
                        if seq_pos!=-1:
                            temp.seq=data[seq_pos]
                        if cdr3_aa_pos!=-1:
                            temp.add_cdr3(data[cdr3_aa_pos])
                        else:
                            temp.add_cdr3("")
                        if dgene_pos!=-1:
                            temp.add_dgene(data[dgene_pos])
                        else:
                            temp.add_dgene("")
                    except:
                        continue
                    temp.get_stats(20,"YDSS")
                    all_foundD+=temp.foundD
                    all_correctLength+=temp.correctLength
                    all_Dgene_ID+=temp.Dgene_ID
                    all_Dgene_position+=temp.Dgene_position
                    all_len_D_pos+=temp.len_D_pos
                    all_functional+=temp.functional
                    outfile.write("%d\t%d\t%d\t%d\t%d\t%d\n"%(temp.Dgene_ID,temp.foundD,temp.correctLength,temp.Dgene_position,temp.len_D_pos,temp.functional))

    #print("D gene ID\tfound D pattern\tcorrect Length\tcorrect position\tcorrect length \& D pos")
    print("%d\t%d\t%d\t%d\t%d\t%d"%(all_Dgene_ID,all_foundD,all_correctLength,all_Dgene_position,all_len_D_pos,all_functional))


if __name__=="__main__":
    if len(sys.argv)==2:
        main(sys.argv[1])
    elif len(sys.argv)>2:
        main(sys.argv[1],sys.argv[2])


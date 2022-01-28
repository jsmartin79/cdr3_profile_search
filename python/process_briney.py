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
    def AddUCA(self,seq):
        self.UCA=seq
    def AddMarkup(self,markupGenes,markup):
        self.markup=markup
        genesplit=markupGenes.split('|')
        for gene in genesplit:
            #print(gene)
            if "V" in gene:
                self.IGHV=gene
            elif "J" in gene:
                self.IGHJ=gene
            elif "D" in gene:
                self.IGHD=gene
               
        #input('e')
    def convertAA(self):
        dna_to_aa=DNAtoAAmap()
        self.UCAAA=[]
        if "-" in self.UCA:
            UCA=self.UCA.replace("-","")
            markup=self.markup.replace("-","")
        else:
            UCA=self.UCA
            markup=self.markup

        cdr3=[]
        markupcdr3=[]
        #print(UCA)
        #print(markup)
        for i,nt in enumerate(markup):
            if nt in ["V","n","D","J"]:
                cdr3.append(UCA[i])
                markupcdr3.append(nt)
                #print("%s-%s"%(nt,UCA[i]))
        #input('e')
        self.cdr3nt="".join(cdr3)
        self.AAmarkup="".join(markupcdr3)
        #[seq[i:i+3] for i in range(0, len(seq), 3)]
        tmp=[]
        for i in range(0, int(len(self.cdr3nt)/3)*3, 3):
            try:
                tmp.append(dna_to_aa[self.cdr3nt[i:i+3]])
            except:
                tmp.append("X")
        
        self.cdr3AA="".join(tmp)


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

        
def DNAtoAAmap():
    dna_to_aa_tranx_map=dict()
    #ALA
    dna_to_aa_tranx_map["GCT"]="A";  
    dna_to_aa_tranx_map["GCC"]="A";  
    dna_to_aa_tranx_map["GCA"]="A";  
    dna_to_aa_tranx_map["GCG"]="A";  
    #ARG
    dna_to_aa_tranx_map["CGT"]="R";  
    dna_to_aa_tranx_map["CGC"]="R";  
    dna_to_aa_tranx_map["CGA"]="R";  
    dna_to_aa_tranx_map["CGG"]="R"; 
    dna_to_aa_tranx_map["AGA"]="R"; 
    dna_to_aa_tranx_map["AGG"]="R"; 
    #ASN
    dna_to_aa_tranx_map["AAT"]="N"; 
    dna_to_aa_tranx_map["AAC"]="N"; 
    #ASP
    dna_to_aa_tranx_map["GAT"]="D"; 
    dna_to_aa_tranx_map["GAC"]="D"; 
    #CYS
    dna_to_aa_tranx_map["TGT"]="C"; 
    dna_to_aa_tranx_map["TGC"]="C"; 
    #GLN
    dna_to_aa_tranx_map["CAA"]="Q"; 
    dna_to_aa_tranx_map["CAG"]="Q"; 
    #GLU
    dna_to_aa_tranx_map["GAA"]="E"; 
    dna_to_aa_tranx_map["GAG"]="E"; 
    #GLY
    dna_to_aa_tranx_map["GGT"]="G"; 
    dna_to_aa_tranx_map["GGC"]="G"; 
    dna_to_aa_tranx_map["GGA"]="G"; 
    dna_to_aa_tranx_map["GGG"]="G"; 
    #HIS
    dna_to_aa_tranx_map["CAT"]="H"; 
    dna_to_aa_tranx_map["CAC"]="H"; 
    #ILE
    dna_to_aa_tranx_map["ATT"]="I"; 
    dna_to_aa_tranx_map["ATC"]="I"; 
    dna_to_aa_tranx_map["ATA"]="I"; 
    #LEU
    dna_to_aa_tranx_map["TTA"]="L"; 
    dna_to_aa_tranx_map["TTG"]="L"; 
    dna_to_aa_tranx_map["CTT"]="L"; 
    dna_to_aa_tranx_map["CTC"]="L"; 
    dna_to_aa_tranx_map["CTA"]="L"; 
    dna_to_aa_tranx_map["CTG"]="L"; 
    #LYS
    dna_to_aa_tranx_map["AAA"]="K"; 
    dna_to_aa_tranx_map["AAG"]="K"; 
    #MET
    dna_to_aa_tranx_map["ATG"]="M"; 
    #PHE
    dna_to_aa_tranx_map["TTT"]="F"; 
    dna_to_aa_tranx_map["TTC"]="F"; 
    #PRO
    dna_to_aa_tranx_map["CCT"]="P"; 
    dna_to_aa_tranx_map["CCC"]="P"; 
    dna_to_aa_tranx_map["CCA"]="P"; 
    dna_to_aa_tranx_map["CCG"]="P"; 
    #SER
    dna_to_aa_tranx_map["TCT"]="S"; 
    dna_to_aa_tranx_map["TCC"]="S"; 
    dna_to_aa_tranx_map["TCA"]="S"; 
    dna_to_aa_tranx_map["TCG"]="S"; 
    dna_to_aa_tranx_map["AGT"]="S"; 
    dna_to_aa_tranx_map["AGC"]="S"; 
    #THR
    dna_to_aa_tranx_map["ACT"]="T"; 
    dna_to_aa_tranx_map["ACC"]="T"; 
    dna_to_aa_tranx_map["ACA"]="T"; 
    dna_to_aa_tranx_map["ACG"]="T"; 
    #TRP
    dna_to_aa_tranx_map["TGG"]="W"; 
    #TYR
    dna_to_aa_tranx_map["TAT"]="Y"; 
    dna_to_aa_tranx_map["TAC"]="Y"; 
    #VAL
    dna_to_aa_tranx_map["GTT"]="V"; 
    dna_to_aa_tranx_map["GTC"]="V"; 
    dna_to_aa_tranx_map["GTA"]="V"; 
    dna_to_aa_tranx_map["GTG"]="V"; 
    #STOP
    dna_to_aa_tranx_map["TAA"]="*"; 
    dna_to_aa_tranx_map["TGA"]="*"; 
    dna_to_aa_tranx_map["TAG"]="*"; 
    
    return dna_to_aa_tranx_map

def main(fastafile,resultsname="results.txt"):
    seqs=[]
    all_foundD=0
    all_correctLength=0
    all_Dgene_ID=0
    all_Dgene_position=0
    all_len_D_pos=0
    all_functional=0
    with open(resultsname,'w') as outfile:
        outfile.write("D gene ID\tfound D pattern\tcorrect Length\tcorrect position\tcorrect length \& D pos\tFunctional\n")
        with open(fastafile,'r') as seqfile:
            linecount=1
            name=""
            seq=""
            ucaseq=""
            markupGenes=""
            markup=""
            for line in seqfile:
                if linecount%6==1:
                    name=line.rstrip()
                elif linecount%6==2:
                    seq=line.rstrip()
                elif linecount%6==3:
                    pass
                elif linecount%6==4:
                    ucaseq=line.rstrip()
                elif linecount%6==5:
                    markupGenes=line.rstrip()
                elif linecount%6==0:
                    markup=line.rstrip()
                    temp=Seq(name,seq)
                    temp.AddUCA(ucaseq)
                    temp.AddMarkup(markupGenes,markup)
                    temp.convertAA()
                    #seqs.append(temp)
                    temp.get_stats(20,"YDSS")

                    all_foundD+=temp.foundD
                    all_correctLength+=temp.correctLength
                    all_Dgene_ID+=temp.Dgene_ID
                    all_Dgene_position+=temp.Dgene_position
                    all_len_D_pos+=temp.len_D_pos
                    all_functional+=temp.functional
                    outfile.write("%d\t%d\t%d\t%d\t%d\t%d\n"%(temp.Dgene_ID,temp.foundD,temp.correctLength,temp.Dgene_position,temp.len_D_pos,temp.functional))
                linecount+=1

    print("D gene ID\tfound D pattern\tcorrect Length\tcorrect position\tcorrect length \& D pos\tFunctional")
    print("%d\t%d\t%d\t%d\t%d\t%d"%(all_Dgene_ID,all_foundD,all_correctLength,all_Dgene_position,all_len_D_pos,all_functional))
    #for seq in seqs:
    #    try:
    #        print("%s,%s"%(seq.name,seq.IGHD))
    #    except:
    #        print("%s,%s"%(seq.name,"-----"))

if __name__=="__main__":
    if len(sys.argv)==2:
        main(sys.argv[1])
    elif len(sys.argv)>2:
        main(sys.argv[1],sys.argv[2])

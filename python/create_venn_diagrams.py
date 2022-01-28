#!/usr/bin/python

#libraries
import xlrd, re
import glob
import os
import string
import sys
import inspect
import numpy,scipy
import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt
from matplotlib_venn import venn3
from matplotlib_venn import venn2

def read_file(infile):
    data_dict=dict()
    with open(infile,'r') as f:
        while True:
            line=f.readline()
            if not line:
                break
            linedata=line.rstrip().split()
            data_dict[linedata[0]]=linedata[1]
    return data_dict

def main(file1,file2,file3,pdfname):
    file1_data=read_file(file1)
    file2_data=read_file(file2)
    file3_data=read_file(file3)

    v=venn3((set(file1_data.keys()),set(file2_data.keys()),set(file3_data.keys())), (file1,file2,file3))
    plt.savefig(pdfname)
    plt.close()

    #print(inspect.getmembers(v))
    data=[]
    for i,t in enumerate(v.subset_labels):
        data.append(t.get_text())
    print("\t".join(data))


    file1_file2=[x for x in file1_data.keys() if x in file2_data.keys()]
    in_all=[x for x in file1_file2 if x in file3_data.keys()]

    #print(in_all)
    with open(pdfname.replace('.pdf','.txt'),'w') as f:
        f.write("sequence\t{}\t{}\t{}\n".format(file1,file2,file3))
        for seq in in_all:
            f.write("{}\t{}\t{}\t{}\n".format(seq,file1_data[seq],file2_data[seq],file3_data[seq]))
    
if __name__=="__main__":
    main(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4])

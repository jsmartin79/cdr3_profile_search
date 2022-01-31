#!/usr/bin/python

#libraries
#import xlrd, re
#import glob
import os
import sys
import itertools
import numpy,scipy
import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt

def AAmap():
    AApos=dict()
    AAlist="ARNDCQEGHILKMFPSTWYVX"
    for i,AA in enumerate(AAlist):
        AApos[AA]=i
    return AApos

def GetColor(value,scale=[]):
    if value<0.333:
        B=1-value
        G=0
        R=0
    elif value<0.666:
        B=1-value
        G=0
        R=value
    else:
        B=0
        G=0
        R=value
        
    color=[R,G,B]

    return color
        
def readMatrixFile(filename,AAmatrix):
    with open(filename,'r') as f:
        lineCounter=0;
        for line in f:
            if line[0]=="A":
                continue
            else:
                for i,count in enumerate(line.split()):
                    AAmatrix[lineCounter,i]=count
            lineCounter=lineCounter+1
    return AAmatrix

def writeMatrixFile(filename,AAmatrix,AApos):
    AAlist=[]
    for i in range(len(AApos)):
        AA=[x for x in AApos.keys() if AApos[x]==i][0]
        AAlist.append(AA)
    
    with open(filename,'w') as f:
        f.write("\t".join(AAlist)+'\n')
        for line in AAmatrix:
            for count in line:
                f.write("%0.0f\t"%count)
            f.write("\n")

def generateHeatMap(filename,AAmatrix,AApos):
    
    AAmatrixScaled=AAmatrix
    for i,line in enumerate(AAmatrix):
        AAmatrixScaled[i]=line/numpy.sum(line)

    AAlist=[]
    for i in range(len(AApos)):
        AA=[x for x in AApos.keys() if AApos[x]==i][0]
        AAlist.append(AA)
    fig,ax=plt.subplots(figsize=((len(AAmatrix[0])+2)/10.0,len(AAmatrix)/10.0+0.1))
    ax.axis('off')
    ax.set_xlim(0,len(AAmatrix[0])/10.0)
    ax.set_ylim(-.1,len(AAmatrix[0])/10.0-0.5)

    for k,base in enumerate(AAlist):
        ax.text(k/10.0-.05,len(AAlist)/10.0+0.03-0.75,base,ha="center",va="bottom",color='black',fontsize=6)

    for i,seq in enumerate(AAmatrixScaled):
        for k,base in enumerate(seq):

            r,g,b=GetColor(AAmatrixScaled[i,k],[0,1])
            text_color = 'white' if r + g + b <= 1.5 else 'black'
            ax.text(k/10.0-0.05,(len(AAlist)-i/1.75)/10.0-0.75,"%0.2f"%base,color=text_color,fontsize=2,ha="center",va="center",bbox={'facecolor':[r,g,b],'alpha':0.5,'pad':1,'edgecolor':'none'})



    plt.savefig(filename.replace(".txt",".pdf"),bbox_inches='tight')
    plt.close(fig)

        
        
def main(outfilename,seq_file_name):
    AApos=AAmap()
    AAmatrix=numpy.zeros((22,len(AApos)))

    if os.path.isfile(outfilename):
        AAmatrix=readMatrixFile(outfilename,AAmatrix)
    
    with open(seq_file_name,'r') as seq_file:
    	 for line in seq_file:
    	     seq=line.split()[0]
             for i,AA in enumerate(seq):
                 AAmatrix[i,AApos[AA]]=AAmatrix[i,AApos[AA]]+1

    writeMatrixFile(outfilename,AAmatrix,AApos)
    generateHeatMap(outfilename,AAmatrix,AApos)
    return 0

if __name__=="__main__":

   if len(sys.argv)>3 and sys.argv[3]=="-r":
       if os.path.isfile(sys.argv[1]):
           os.remove(sys.argv[1])
       
   main(sys.argv[1],sys.argv[2])       

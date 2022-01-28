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
import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt
import writeTable

def GenerateBins(data_list):
    bins=numpy.zeros([1,21])
    data=numpy.array(data_list)
    for i in range(0,21):
        bins[0,i]=len(data[data==i])/float(len(data_list))
    return bins

def color_lookup(v):
    c=[247,252,240]

    #print(v)
    #if v<1/1000000000.0:

    if   v<=1/1000000000.0:
        #c=[247,252,240]
        c=[235,255,230]
    elif v<=1/100000000.0:
        c=[224,243,219]
    elif v<=1/10000000.0:
        c=[204,235,197]
    elif v<=1/1000000.0:
        c=[168,221,181]
    elif v<=1/100000.0:
        c=[123,204,196]
    elif v<=1/10000.0:
        c=[78,179,211]
    elif v<=1/1000.0:
        c=[43,140,190]
    elif v<=1/100.0:
        #c=[8,88,158]
        c=[8,104,172]
    else:
        c=[8,64,129]

    #f7fcf0
    #e0f3db
    #ccebc5
    #a8ddb5
    #7bccc4
    #4eb3d3
    #2b8cbe
    #08589e
    
    #247,252,240
    #224,243,219
    #204,235,197
    #168,221,181
    #123,204,196
    #78,179,211
    #43,140,190
    #8,88,158
    return [i/255.0 for i in c]

def plot_heatmap(outpdf,data):
    plt.clf()
    fig,ax=plt.subplots(figsize=(10,10))
    ax.axis('tight')

    ax.set_ylim(-0.5,data.shape[0]-0.5)
    ax.set_xlim(-0.5,data.shape[1]-0.5)
    #ax.imshow(data)
    for i,vec_thresh in enumerate(data):
        for n,data in enumerate(vec_thresh):
            if data==0:
                color=[1,1,1]
            else:
                color=color_lookup(data)
            rect=plt.Rectangle((n-0.5,i-0.5),1,1,fc=color,ec="black")
            ax.add_patch(rect)
    ax.set_yticks(range(0,len([x/5.0 for x in range(-15,1)])))
    ax.set_yticklabels(["{0:.2f}".format(x/5.0) for x in range(-15,1)])
    
    ax.set_xticks(range(0,21))
    #ax.set_xticks(range(0,14))
    ax.grid(b=None)
    plt.grid(b=None)
    plt.xlabel("Amino Acid Distance")
    plt.ylabel("Matrix Threshold Value")
    #plt.title("heatmap")
    #plt.xlim(0,0.30)
    #plt.grid(False)
    plt.savefig(outpdf,bbox_inches='tight')
    plt.close("all")

def plot_cum_heatmap(outpdf,data):
    plt.clf()
    fig,ax=plt.subplots(figsize=(10,10))
    ax.axis('tight')

    ax.set_ylim(-0.5,data.shape[0]-0.5)
    ax.set_xlim(-0.5,data.shape[1]-0.5)
    for i,vec_thresh in enumerate(data):
        #print(vec_thresh)
        cum_data=0
        for n,data in enumerate(vec_thresh):
            cum_data+=data
            #print(cum_data)
            if cum_data==0:
                color=[1,1,1]
            else:
                color=color_lookup(cum_data)
                
            rect=plt.Rectangle((n-0.5,i-0.5),1,1,fc=color,ec="black")
            ax.add_patch(rect)
            #print(data)
        #input('e')
    ax.set_yticks(range(0,len([x/5.0 for x in range(-15,1)])))
    ax.set_yticklabels(["{0:.2f}".format(x/5.0) for x in range(-15,1)])
    
    ax.set_xticks(range(0,21))
    ax.set_xticklabels(["$\leq${}".format(x) for x in range(0,21)])
    ax.grid(b=None)
    plt.grid(b=None)
    plt.xlabel("Amino Acid Distance (cumulative)")
    plt.ylabel("Matrix Threshold Value")
    #plt.title("heatmap")
    #plt.xlim(0,0.30)
    #plt.grid(False)
    plt.savefig(outpdf,bbox_inches='tight')
    plt.close("all")
    
def plot_legend(outpdf):
    fig,ax=plt.subplots(figsize=(3,5))

    ax.axis('off')

    ax.set_ylim(-0.5,10.5)
    ax.set_xlim(-0.5,6.5)
    values=[10,100,1000,10000,100000,1000000,10000000,100000000,1000000000,0]
    for i,data in enumerate(values):

        if data==0:
            color=[1,1,1]
            ax.text(1.5,i+0.5,"Not Detected".format(data))
        else:
            color=color_lookup(0.9/data)
            if i==8:
                ax.text(1.5,i+0.5,"$\leq$ 1 in {:,d}".format(data))
            else:
                ax.text(1.5,i+0.5,"> 1 in {:,d}".format(values[i+1]))

        rect=plt.Rectangle((0.0,i),1,1,fc=color,ec="black")
        ax.add_patch(rect)

    
    plt.savefig(outpdf,bbox_inches='tight')
    plt.close("all")

def main(filename,outname):
    threshold_list=[x/5.0 for x in range(-15,1)]
    distanceHash=dict()
    for T in threshold_list:
        distanceHash[T]=numpy.zeros([1,21])
    with open(filename, "r") as infile:
        while True:
            line=infile.readline()
            if not line:
                break
            dataline=line.rstrip().split()
            for i,value in enumerate(dataline[1:]):
                distanceHash[threshold_list[i]][0,int(value)]+=1
    heatmap=numpy.zeros([len(threshold_list),21])

    for i,T in enumerate(threshold_list):
        #heatmap[i,:]=GenerateBins(distanceHash[T])
        fullCount=numpy.sum(distanceHash[T])
        #fullCount=107337185#functional
        #print(distanceHash[T][0,:])
        print("standard scaling {}".format(fullCount))
        for pos,n in enumerate(distanceHash[T][0,:]):
            heatmap[i,pos]=n/fullCount
        #print(heatmap)
        #input('e')
    plot_heatmap(outname,heatmap)
    writeTable.writeTable(outname.replace(".pdf",".table.txt"),heatmap,[x/5.0 for x in range(-15,1)])
    plot_cum_heatmap(outname.replace(".pdf",".cumulative.pdf"),heatmap)

    heatmap=numpy.zeros([len(threshold_list),21])

    for i,T in enumerate(threshold_list):
        #heatmap[i,:]=GenerateBins(distanceHash[T])
        #fullCount=numpy.sum(distanceHash[T])
        
        fullCount=85149053#functional, uniq briney number
        #fullCount=2452900000000#generated igor plots functional adjusted

        print("briney scaling {}".format(fullCount))
        #print(distanceHash[T][0,:])
        #print(heatmap)
        for pos,n in enumerate(distanceHash[T][0,:]):
            heatmap[i,pos]=n/fullCount
        #print(heatmap)
        #input('e')
    plot_heatmap(outname.replace(".pdf",".Briney_scale.pdf"),heatmap)
    writeTable.writeTable(outname.replace(".pdf",".Briney_scale.table.txt"),heatmap,[x/5.0 for x in range(-15,1)])   
    plot_cum_heatmap(outname.replace(".pdf",".Briney_scale.cumulative.pdf"),heatmap)
    
    plot_legend("legend.pdf")
    
if __name__=="__main__":
    #argument 1 is filename
    #argument 2 is the scoring matrix

        main(sys.argv[1],sys.argv[2])

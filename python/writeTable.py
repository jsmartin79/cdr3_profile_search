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

def writeTable(outname,data,Vect):#need to reverse the data
    thresholdVect=Vect[::-1]
    with open(outname,'w') as outfile:
        for i,vec_thresh in enumerate(data[::-1]):
            outfile.write("{}\t".format(thresholdVect[i]))
            for n,values in enumerate(vec_thresh):
                outfile.write("{:0.4e}\t".format(values))
            outfile.write("\n")
        outfile.write("\n")
        outfile.write(" ")
        for i in range(len(data[0])):
            outfile.write("\t{}".format(i))
        outfile.write("\n")

        
                            

#!/bin/python
import numpy


file=open("CH235_logfoldChange_all_AA.txt",'r')

lines=file.readlines()

matrix=[]
for line in lines[1:]:
    matrix.append(line.rstrip().split('\t')[3:])

count=[]

for i in range(13):
    print("pos:%d"%i)
    count.append(0)
    for line in matrix:
        if float(line[i])>-0.2:
            count[i]+=1
    print(count[i])

print("pos\tcount\tpercent")
for i in range(13):
    print("%d\t%d\t%f"%(i+1,count[i],float(count[i])/20.0))

product=numpy.product([float(x)/20.0 for x in count])
print(product)

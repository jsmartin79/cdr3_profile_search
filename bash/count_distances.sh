#!/bin/bash
#SBATCH --job-name=count
#SBATCH --out count-%j.out
#SBATCH --ntasks=1
#SBATCH --mem=50G
#SBATCH --partition=dhvi
#SBATCH --ntasks-per-node=1

filename=${1}

for i in $(seq 2 17)
do
    rm -rf /tmp/*
    echo "column position" ${i}
    cut -f ${i} ${filename} | sort | uniq -c > counts_${i}.txt
    sort -k2 -n counts_${i}.txt > tmp
    mv tmp counts_${i}.txt
done

cp counts_16.txt "counts_for_-0.2.txt"

#!/bin/bash
#SBATCH --job-name=countZeros
#SBATCH --ntasks=1
#SBATCH --error=slurm-%j.err
#SBATCH --mem=25G
#SBATCH --partition=dhvi
#SBATCH --ntasks-per-node=1


for i in $(seq 2 22)
do
    B=$(cut -f 1,${i} igor_dist.temp.txt | grep -w 0 | wc -l)
    GN=$(cut -f 1,${i} Igor_GN_distance.txt | grep -w 0 | wc -l)
    GS=$(cut -f 1,${i} Igor_GS_distance.txt | grep -w 0 | wc -l)
    
    echo ${B} ${GN} ${GS} >> distance_counts.txt
done

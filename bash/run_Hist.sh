#!/bin/bash
#SBATCH --job-name=Rhist
#SBATCH --out=SeqScoring-%j.out
#SBATCH --ntasks=1
#SBATCH --mem=20G
#SBATCH --partition=dhvi
#SBATCH --ntasks-per-node=1

Rscript histogram.r >  stat_data.txt

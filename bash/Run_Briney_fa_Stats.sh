#!/bin/bash
#SBATCH --job-name=getRaw
#SBATCH --out=getRaw-%j.out
#SBATCH --ntasks=1
#SBATCH --mem=16G
#SBATCH --partition=dhvi
#SBATCH --ntasks-per-node=1
#SBATCH --exclude=dcc-dhvi-0[5-7]

#>Briney_D_gene_stats.txt

python3 process_briney.py Briney_sequences.RC.SMUA.fasta > Briney_cloanalyst_D_gene_stats.txt




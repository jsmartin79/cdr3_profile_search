#!/bin/bash
#SBATCH --job-name=getRaw
#SBATCH --out=getRaw-%j.out
#SBATCH --ntasks=1
#SBATCH --mem=16G
#SBATCH --partition=dhvi
#SBATCH --ntasks-per-node=1
#SBATCH --exclude=dcc-dhvi-0[5-7]

#>Briney_D_gene_stats.txt

for file in $(find /datacommons/dhvi/Briney_dataset -iname "*consensus.txt")
do
python3 process_briney_directly.py ${file} >> Briney_D_gene_stats.txt
done



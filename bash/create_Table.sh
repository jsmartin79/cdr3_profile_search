#!/bin/bash
#SBATCH --job-name=countZeros
#SBATCH --ntasks=1
#SBATCH --error=slurm-%j.err
#SBATCH --mem=25G
#SBATCH --partition=dhvi
#SBATCH --ntasks-per-node=1
#SBATCH --exclude=dcc-dhvi-[09,10,11]  

#sbatch Run_Scoring.sh -s /datacommons/dhvi/Generated_cdr3_seqs/seq_w_D.txt.gz

sort logfoldChange_small_distance.txt | uniq > tmp_dist_file.txt

file=tmp_dist_file.txt

numb_col=$(head -n 1 ${file} | tr "\t" "\n" | wc -l )

for i in $(seq 2 ${numb_col})
do
    
    cut -f ${i} ${file} | sort | uniq -c  > column_table_${i}.txt
done


#cat x*.split.dist > logfoldChange_tmp.txt

sort logfoldChange_tmp.txt | uniq > tmp_dist_file.txt

file=tmp_dist_file.txt

numb_col=$(head -n 1 ${file} | tr "\t" "\n" | wc -l )

for i in $(seq 2 ${numb_col})
do

    cut -f ${i} ${file} | sort | uniq -c  > column_table_${i}_tmp.txt
done

rm ${file}

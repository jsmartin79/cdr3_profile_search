#!/bin/bash
#SBATCH --job-name=SeqScoring
#SBATCH --out=SeqScoring-%j.out
#SBATCH --ntasks=1
#SBATCH --mem=10G
#SBATCH --partition=dhvi
#SBATCH --ntasks-per-node=1
#SBATCH --exclude=dcc-dhvi-0[4-6]

#> Briney_CDR3.txt
#
#for file in $(find /datacommons/dhvi/Briney_dataset -iname "*consensus.txt")
#do
#col=$(head -n 1 ${file} | tr "," "\n" | nl | tr -s " " "\t" | grep "cdr3_aa" | cut -f 2)
#
#echo ${file} ${col}
#cut -f ${col} -d "," ${file} > tmp.txt
#grep -v "cdr3_aa" tmp.txt | grep -v "X" > tmp
#sed -i '/^$/d' tmp
#sort tmp | uniq > tmp.txt
#cat tmp.txt >> Briney_CDR3.txt
#done


split -l 10000000 --additional-suffix=.txt.split -d -a 6  Briney_CDR3.txt

for file in $(find . -iname "*.txt.split")
do
	mv ${file} ${file/x0/CH235}
	sbatch /work/jsmb/score/CH235_Briney/process_Briney.job ${file/x0/CH235}
done

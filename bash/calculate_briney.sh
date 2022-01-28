#!/bin/bash
#SBATCH --job-name=BrineyCounts
#SBATCH --out=BrineyCounts-%j.out
#SBATCH --ntasks=1
#SBATCH --mem=32G
#SBATCH --partition=dhvi
#SBATCH --ntasks-per-node=1


> Briney_CDR3_cleancounts.txt
#
for file in $(find /datacommons/dhvi/Briney_dataset -iname "*consensus.txt")
do
col=$(head -n 1 ${file} | tr "," "\n" | nl | tr -s " " "\t" | grep "cdr3_aa" | cut -f 2)

echo ${file} ${col}
cut -f ${col} -d "," ${file} > tmp.txt
grep -v "cdr3_aa" tmp.txt  > tmp
sed -i '/^$/d' tmp
cat tmp >> Briney_CDR3_cleancounts.txt
done

echo "full counts:" $(wc -l Briney_CDR3_cleancounts.txt)

sort Briney_CDR3_cleancounts.txt | uniq > Briney_CDR3_uniq.txt

echo "uniq full counts" $(wc -l Briney_CDR3_uniq.txt)

echo "numb functional:" $(grep -v "*" Briney_CDR3_cleancounts.txt | wc -l)
echo "numb non-functional:" $(grep "*" Briney_CDR3_cleancounts.txt | wc -l)

echo "numb functional (uniq):" $(grep -v "*" Briney_CDR3_uniq.txt | wc -l)
echo "numb non-functional (uniq):" $(grep "*" Briney_CDR3_uniq.txt | wc -l)

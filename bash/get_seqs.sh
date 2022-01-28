#!/bin/bash
#SBATCH --job-name=count_seqs
#SBATCH --out=count_seqs-%j.out
#SBATCH --ntasks=1
#SBATCH --mem=10G
#SBATCH --partition=dhvi
#SBATCH --ntasks-per-node=1

outfile="outfile.stats"
> ${outfile}
> simplified_${outfile}
#for file in $(find /datacommons/dhvi/Briney_dataset -iname "*consensus.txt")
#do
#    rename=$(echo ${file}  | cut -f 5- -d "/" | tr "/" "_")
#    echo ${rename}
#    cp ${file} ${rename}
#done

#file=${1}
for file in *consensus.txt.gz
do
 gzip -d ${file}
done


for file in *consensus.txt
do
    
    AAcol=$(head -n 1 ${file} | tr "," "\n" | nl | tr -s " " "\t" | grep "cdr3_aa" | cut -f 2)
    NTcol=$(head -n 1 ${file} | tr "," "\n" | nl | tr -s " " "\t" | grep "cdr3_nt" | cut -f 2)

    if [ -z ${NTcol+x} ];
    then
	cut ${file} -d ',' -f 1,${AAcol} | tr "," "\t" > ${file/txt/aa}
	cut ${file} -d ',' -f 1 | tr "," "\t" > ${file/txt/nt}
    else
	cut ${file} -d ',' -f 1,${AAcol} | tr "," "\t" > ${file/txt/aa}
	cut ${file} -d ',' -f 1,${NTcol} | tr "," "\t" > ${file/txt/nt}
    fi	

    
    tail -q -n +2 ${file/txt/aa} > junk.aa
    tail -q -n +2 ${file/txt/nt} > junk.nt
    
    nt=$(cut junk.nt -f 2 | grep -P '\S' | wc -l)
    ntU=$(cut junk.nt -f 2 | grep -P '\S' | sort | uniq | wc -l)
    aa=$(cut junk.aa -f 2 | grep -P '\S' | wc -l)
    aaU=$(cut junk.aa -f 2 | grep -P '\S' | sort | uniq | wc -l )
    aaUFunc=$(cut junk.aa -f 2 | grep -P '\S' | grep -v '*' | sort | uniq | wc -l )
    
    echo ${file} ${nt} ${ntU} ${aa} ${aaU} ${aaUFunc} >> ${outfile}
done

for name in $(ls *consensus.txt | cut -f 1 -d '_' | sort | uniq)
do
    tail -q -n +2 ${name}*consensus.aa > ${name}.aa
    tail -q -n +2 ${name}*consensus.nt > ${name}.nt

    nt=$(cut ${name}.nt -f 2 | grep -P '\S' | wc -l)
    ntU=$(cut ${name}.nt -f 2 | grep -P '\S' | sort | uniq | wc -l)
    aa=$(cut ${name}.aa -f 2 | grep -P '\S' | wc -l)
    aaU=$(cut ${name}.aa -f 2 | grep -P '\S' | sort | uniq | wc -l )
    aaUFunc=$(cut ${name}.aa -f 2 | grep -P '\S' | grep -v '*' | sort | uniq | wc -l )

    echo ${name} ${nt} ${ntU} ${aa} ${aaU} ${aaUFunc} >> simplified_${outfile}

done

for file in *consensus.txt
do
 gzip ${file}
done

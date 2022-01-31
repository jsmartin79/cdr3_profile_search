#!/bin/bash

if [ "$#" -le 1 ]; then
    echo "no arguments given"
    exit
fi
for var in "$@"
do
    fastafile=${var}
    weblogo -S 1 --units probability -c chemistry -n 150 --format pdf -P "" --color red ED 'neg' --color purple QN '' --color blue KHR '' --color green SGCYT '' --color black VLPFWAIM '' -a ACDEFGHIKLMNPQRSTVWXY -f ${fastafile} -o ${fastafile/fasta/pdf} --stack-width 500
done

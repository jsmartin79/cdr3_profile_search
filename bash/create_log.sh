#!/bin/bash

weblogo -S 1 --units probability -c chemistry -n 150 --format pdf -P "" --color red ED 'neg' --color purple QN '' --color blue KHR '' --color green SGCYT '' --color black VLPFWAIM '' -a ACDEFGHIKLMNPQRSTVWXY -f 15count.fasta  -o 15count.pdf

weblogo -S 1 --units probability -c chemistry -n 150 --format logodata -P "" --color red ED 'neg' --color purple QN '' --color blue KHR '' --color green SGCYT '' --color black VLPFWAIM '' -a ACDEFGHIKLMNPQRSTVWXY -f 15count.fasta  -o 15count_table.txt

weblogo -S 1 --units probability -c chemistry -n 150 --format pdf -P "" --color red ED 'neg' --color purple QN '' --color blue KHR '' --color green SGCYT '' --color black VLPFWAIM '' -a ACDEFGHIKLMNPQRSTVWXY -f 20count.fasta  -o 20count.pdf

weblogo -S 1 --units probability -c chemistry -n 150 --format logodata -P "" --color red ED 'neg' --color purple QN '' --color blue KHR '' --color green SGCYT '' --color black VLPFWAIM '' -a ACDEFGHIKLMNPQRSTVWXY -f 20count.fasta  -o 20count_table.txt


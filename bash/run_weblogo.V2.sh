#!/bin/bash

weblogo -S 1 --units probability -c chemistry -n 150 --format pdf -P "" --color red ED 'neg' --color purple QN '' --color blue KHR '' --color green SGCYT '' --color black VLPFWAIM '' -a ACDEFGHIKLMNPQRSTVWXY -f madeSeq.fasta -o madeSeq.V2.pdf --stack-width 500

weblogo -S 1 --units probability -c chemistry -n 150 --format pdf -P "" --color red ED 'neg' --color purple QN '' --color blue KHR '' --color green SGCYT '' --color black VLPFWAIM '' -a ACDEFGHIKLMNPQRSTVWXY -f Briney_CDR3.FUD.fasta -o Briney.V2.pdf --stack-width 500

weblogo -S 1 --units probability -c chemistry -n 150 --format pdf -P "" --color red ED 'neg' --color purple QN '' --color blue KHR '' --color green SGCYT '' --color black VLPFWAIM '' -a ACDEFGHIKLMNPQRSTVWXY -f igor_generated.fasta -o ior_generated.V2.pdf --stack-width 500

weblogo -S 1 --units probability -c chemistry -n 150 --format pdf -P "" --color red ED 'neg' --color purple QN '' --color blue KHR '' --color green SGCYT '' --color black VLPFWAIM '' -a ACDEFGHIKLMNPQRSTVWXY -f DH270_generated_seqs.fasta -o DH270_generated.V2.pdf --stack-width 500

weblogo -S 1 --units probability -c chemistry -n 150 --format pdf -P "" --color red ED 'neg' --color purple QN '' --color blue KHR '' --color green SGCYT '' --color black VLPFWAIM '' -a ACDEFGHIKLMNPQRSTVWXY -f regened_Logo.fasta.fasta -o generated_logo.V2.pdf --stack-width 500

#weblogo -S 1 --units probability -c chemistry -n 150 --format pdf -P "" --color red ED 'neg' --color purple QN '' --color blue KHR '' --color green SGCYT '' --color black VLPFWAIM '' -a ACDEFGHIKLMNPQRSTVWXY -f CH235_gen_seq.fasta -o CH235_generated.pdf

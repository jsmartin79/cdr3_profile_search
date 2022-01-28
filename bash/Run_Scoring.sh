#!/bin/bash
#SBATCH --job-name=SeqScoring
#SBATCH --out=SeqScoring-%j.out
#SBATCH --ntasks=1
#SBATCH --mem=20G
#SBATCH --partition=dhvi
#SBATCH --ntasks-per-node=1
#SBATCH --exclude=dcc-dhvi-0[4-6]

maxjobs=1000
BREAK=false
numberLines=1000000

#call getopt to validate the provided input
options=$(getopt -o hs:r:f:m:l: --long thread: -- "$@")

eval set -- "$options"
while true;
do
  	case "${1}" in
	-h)
		echo "program for runnign the scoring issues"
		;;
	-s)
	#split file
		infile=${2}
		shift 2
		BREAK=true
		SCORE=false
		;;
	-l)
	    numberLines=${2}
	    shift 2
	    ;;
	-m)
	    maxjobs=${2}
	    shift 2
	    ;;
	-r)
	#run files
		infile=${2}
		echo ${infile}
		#python3 ~/seq_scoring/igor_scoring.py ${infile} ~/seq_scoring/scoring_matrix.ALV.txt
		#python3 ~/seq_scoring/seq_distance_calculations.py ${infile} ~/seq_scoring/scoring_matrix.ALV.txt
		#python3 ~/seq_scoring/seq_distance_calculations.py ${infile} ~/seq_scoring/GN_logodd_matrix.txt
		python3 ~/seq_scoring/seq_distance_calculations.py ${infile} ~/seq_scoring/DH270_logfoldChange.txt

		#rm ${infile}
		shift 2
		;;
	-f)
	#run files
		infile=${2}
		echo ${infile}
		#python3 ~/seq_scoring/igor_scoring.py ${infile} ~/seq_scoring/scoring_matrix.ALV.txt
		#python3 ~/seq_scoring/seq_distance_calculations.py ${infile} ~/seq_scoring/scoring_matrix.ALV.txt
		#python3 ~/seq_scoring/seq_distance_calculations.py ${infile} ~/seq_scoring/GN_logodd_matrix.txt
		python3 ~/seq_scoring/seq_distance_calculations.py ${infile} ~/seq_scoring/DH270_logfoldChange.txt
		#rm ${infile}
		shift 2
		;;
	--thread)
		number=${2}
		echo ${number}
		shift 2
		;;
	--)
		shift
		break
		;;
	esac
done

if $BREAK
then
    zcat ${infile} | split -l ${numberLines} --additional-suffix=.txt.split -d -a 6
    
    for file in $(find . -iname "*.txt.split")
    do
        jobcount=$(squeue -p dhvi | grep "SeqScoring" | wc -l)
        while [ ${jobcount} -ge ${maxjobs} ] #while loop to trap process until number of jobs decrease below max number                                                                    
        do
            jobcount=$(squeue -p dhvi | grep "SeqScoring" | wc -l)
        done
	
        gzip ${file}
        sbatch ./Run_Scoring.sh -r ${file}.gz
    done
fi

echo "DONE!"

#!/bin/bash


if (( $# < 3 )); then
	numbSeq=250000000
else
	numbSeq=${3}
fi



startNumb=${1}
echo ${startNumb}
endNumb=${2}
#`expr ${startNumb} + 4`
echo ${endNumb}
for i in $(seq ${startNumb} 1 ${endNumb})
do
	label=$(head /dev/urandom | tr -dc A-Z0-9 |head -c 4;echo '')
	sbatch --partition=dhvi --job-name=igor_runs igor_runs.job ${label} ${numbSeq}
	#echo ${i}
done 


#echo "running collections"
sbatch --dependency=singleton --job-name=igor_runs collect.job


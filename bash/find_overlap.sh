#!/bin/bash

for i in -2.0 -1.0 -0.5 -0.25 0.0; do
    echo "new set"
    echo ${i}
    
cut -f 1 Briney_GS_distance_wD.txt.${i}.top100 > GS.tmp
cut -f 1 Briney_GN_distance_wD.txt.${i}.top100 > GN.tmp
cut -f 1 Briney_distances.txt.${i}.top100 > orig.tmp

echo "GS vs GN" $(grep -f GS.tmp GN.tmp | wc -l)
echo "GS vs orgin" $(grep -f GS.tmp orig.tmp | wc -l)
echo "GN vs orgin" $(grep -f GN.tmp orig.tmp | wc -l)

echo "overlaps"
echo "GS - origin"
grep -f GS.tmp orig.tmp > overlap
echo "GN - origin"
grep -f GN.tmp orig.tmp > overlap
echo "GS - GN"
grep -f GS.tmp GN.tmp > overlap

#echo "GS"
#grep -f overlap Briney_GS_distance_wD.txt.${i}.top100
#echo "GN"
#grep -f overlap Briney_GN_distance_wD.txt.${i}.top100
#echo "orig"
#grep -f overlap Briney_distances.txt.${i}.top100

done

printf "all\tO\tGS\tOuGS\tGN\tOuGN\tGSuGN\tOuGSuGN\n"
for i in -2.0 -1.0 -0.5 -0.25 0.0; do 
python3 create_venn_diagrams.py Briney_distances.txt.${i}.top100 Briney_GS_distance_wD.txt.${i}.top100 Briney_GN_distance_wD.txt.${i}.top100 Thresh${i}.pdf
done

printf "only L\tO\tGS\tOuGS\tGN\tOuGN\tGSuGN\tOuGSuGN\n"
for i in -2.0 -1.0 -0.5 -0.25 0.0; do 
python3 create_venn_diagrams.py Briney_distances.txt.${i}.L.top100 Briney_GS_distance_wD.txt.${i}.L.top100 Briney_GN_distance_wD.txt.${i}.L.top100 Thresh${i}.L.pdf 
done

printf "ALV\tO\tGS\tOuGS\tGN\tOuGN\tGSuGN\tOuGSuGN\n"
for i in -2.0 -1.0 -0.5 -0.25 0.0; do 
python3 create_venn_diagrams.py Briney_distances.txt.${i}.ALV.top100 Briney_GS_distance_wD.txt.${i}.ALV.top100 Briney_GN_distance_wD.txt.${i}.ALV.top100 Thresh${i}.ALV.pdf 
done


cat *.top100 | sort -k2 -r -n | grep -v "-" | cut -f 1 | sort | uniq > pos_values.txt
echo "any AA"
for i in -2.0 -1.0 -0.5 -0.25 0.0; do
    echo ${i}
while read name ; do
    echo ${name} $(grep ${name} Briney_distances.txt.${i}.top100) "t" $(grep ${name} Briney_GS_distance_wD.txt.${i}.top100) "t" $(grep ${name} Briney_GN_distance_wD.txt.${i}.top100);
done < pos_values.txt

done

echo "only L"
for i in -2.0 -1.0 -0.5 -0.25 0.0; do
    echo ${i}
while read name ; do
    echo ${name} $(grep ${name} Briney_distances.txt.${i}.L.top100) "t" $(grep ${name} Briney_GS_distance_wD.txt.${i}.L.top100) "t" $(grep ${name} Briney_GN_distance_wD.txt.${i}.L.top100);
done < pos_values.txt

done

echo "ALV"
for i in -2.0 -1.0 -0.5 -0.25 0.0; do
    echo ${i}
while read name ; do
    echo ${name} $(grep ${name} Briney_distances.txt.${i}.ALV.top100) "t" $(grep ${name} Briney_GS_distance_wD.txt.${i}.ALV.top100) "t" $(grep ${name} Briney_GN_distance_wD.txt.${i}.ALV.top100);
done < pos_values.txt

done

#this loop finds how many time the sequences are found
while read name ; do
    echo ${name} $(grep ${name} *.top100 | sort | uniq | wc -l )
done < pos_values.txt


cat *.top100 | cut -f 1 | sort | uniq > tmp_seqs
>counts
while read seq; do echo ${seq} $(grep -l ${seq} *.top100 | wc -l) >> counts; done < tmp_seqs
sort -k2 -r -n counts | head -n 30
sort -k2 -r -n counts | head -n 30 | cut -f 1 -d " " > list

> tmp
while read seq;
do
    echo ${seq} >> tmp
    grep ${seq} *.top100 >> tmp
    done < list

grep -v "-" tmp

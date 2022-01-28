#!/bin/bash


for i in $(seq 2 22)
do
    B=$(cut -f 1,${i} ../data/Briney_distances_wD.txt | grep -w 0 | wc -l)
    GN=$(cut -f 1,${i} Briney_GN_distance_wD.txt | grep -w 0 | wc -l)
    GS=$(cut -f 1,${i} Briney_GS_distance_wD.txt | grep -w 0 | wc -l)
    ALV=$(cut -f 1,${i} ../data/Briney_distances_wD.ALV.txt | grep -w 0 | wc -l)
    
    echo ${B} ${ALV} ${GN} ${GS}
done

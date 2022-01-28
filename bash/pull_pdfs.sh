#!/bin/bash

rsync -av cluster:/work/jsmb/score/igor_recalc/*.pdf . 
rsync -av cluster:/work/jsmb/score/CH235_Briney/*.pdf . 
rsync -av cluster:/work/jsmb/score/Briney/*.pdf . 

rsync -av cluster:/work/jsmb/score/igor_recalc/*.table.txt . 
rsync -av cluster:/work/jsmb/score/CH235_Briney/*.table.txt . 
rsync -av cluster:/work/jsmb/score/Briney/*.table.txt . 
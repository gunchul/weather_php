#!/bin/bash

YEAR=`date +%Y`
DATE=`date +%Y-%m-%d`
AREAS=("newcastle" "sydney" "wollongong")
OUTPUTS=("newcastle" "bondi" "wollongong")
NUM_AREAS=${#AREAS[@]}

mkdir -p output/${YEAR}

for (( i=0; i<${NUM_AREAS}; i++ ));
do
    python3 weather.py ${AREAS[$i]} > output/${YEAR}/${DATE}_${OUTPUTS[$i]}.txt
done

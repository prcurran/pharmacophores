#!/bin/bash
conda activate hotspots

#'akt1' 'ampc' 'cp3a4' 'cxcr4' 'gcr' 'hivpr' 'hivrt' 'kif11'
for target in 'hivpr'
do
  for num in {3..5}
  do
    nohup python search.py "$target" "$num" > "${target}_${num}.err" 2> "${target}_${num}.out" &
  done
done

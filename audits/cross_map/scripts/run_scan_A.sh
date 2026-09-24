#!/bin/bash
set -e
OUT=../data/scan_A_raw; mkdir -p $OUT
LIM=200000000000; W=8; CH=$((LIM / W))
for i in $(seq 0 $((W-1))); do
  S=$((i * CH + 1)); E=$(((i+1) * CH + 1))
  ./scan_rare 3 1 $S $E > $OUT/part_$i.txt &
done
wait
echo ALLDONE > $OUT/DONE

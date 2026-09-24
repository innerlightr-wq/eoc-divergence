#!/bin/bash
# Parallel rare-side record scan for D = 5x-1 over [1, 10^12), 8 workers.
set -e
OUT=../data/scan_D_raw
mkdir -p $OUT
LIM=1000000000000
W=8
CH=$((LIM / W))
for i in $(seq 0 $((W-1))); do
  S=$((i * CH + 1)); E=$(((i+1) * CH + 1))
  ./scan_rare 5 -1 $S $E > $OUT/part_$i.txt &
done
wait
echo ALLDONE > $OUT/DONE

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
  ./scan_rare 5 -1 $S $E > $OUT/part_$i.txt 2> $OUT/guard_$i.txt &
done
wait
cat $OUT/guard_*.txt          # must be all-zero: a fired guard makes a depth a lower bound
echo ALLDONE > $OUT/DONE

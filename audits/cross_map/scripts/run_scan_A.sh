#!/bin/bash
set -e
OUT=../data/scan_A_raw; mkdir -p $OUT
LIM=200000000000; W=8; CH=$((LIM / W))
for i in $(seq 0 $((W-1))); do
  S=$((i * CH + 1)); E=$(((i+1) * CH + 1))
  ./scan_rare 3 1 $S $E > $OUT/part_$i.txt 2> $OUT/guard_$i.txt &
done
wait
cat $OUT/guard_*.txt          # must be all-zero: a fired guard makes a depth a lower bound
echo ALLDONE > $OUT/DONE

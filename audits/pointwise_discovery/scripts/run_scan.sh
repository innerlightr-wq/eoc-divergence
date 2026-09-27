#!/usr/bin/env bash
# Parallel depth scan.  Usage: run_scan.sh <q> <r> <BITS> <deep> <ncap> <tag>
set -e
q=$1; r=$2; BITS=$3; deep=$4; ncap=$5; tag=$6
END=$((1<<BITS)); J=8; CH=$((END/J))
D=results/scan_$tag; mkdir -p "$D"
for ((i=0;i<J;i++)); do
  s=$((i*CH+1)); e=$(( (i==J-1) ? END : (i+1)*CH ))
  "$(dirname "$0")"/depth_scan "$q" "$r" "$s" "$e" "$deep" "$ncap" > "$D/part_$i.txt" &
done
wait
echo "done $tag"

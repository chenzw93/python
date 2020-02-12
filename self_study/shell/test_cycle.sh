#!/usr/bin/env bash
nums=$1
result=0

for i in {1..$nums..2}
  do
    let result=$result+$i
  done
echo $result
for i in $($nums)
  do
    $result+=$i
  done
echo $result
#!/usr/bin/env bash

first=$1
sec=$2
third=$3

[ ! $#  -ge 3  ] &&  echo "please input three number or more number!" && exit 2

for i in $*
do
  expr $i + 1  &> /dev/null
 [  $?  -ne  0  ] && echo "input is error" && exit
done

#      a=`cat file |xargs -n1|sort -n|head -1`
#      b=`cat file |xargs -n1|sort -n|tail -1`
#      c=`cat file |xargs -n1|sort -n|wc -l`
#
#     d=`cat file |xargs -n1|awk '{a+=$1}'END'{print a}'`

echo "first: $first"
echo "sec: $sec"
echo "third: $third"
#
##[ $b -ne 0 ] &&
#echo "max number:"$b
##[ $a -ne 0 ] &&
#
# echo "min number:"$a
#
#echo "average is:" `awk 'BEGIN{printf "%.2f\n", '$d'/'$c'}'`
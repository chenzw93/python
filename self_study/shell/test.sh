#!/bin/env bash
read -p "请输入第一个参数: " first_param
echo $first_param
#a=1
#b=2
echo $cwd
current_path="$PWD"
echo $current_path

pys=$(ls "$PWD" | grep *.py)
echo $pys

path=$(find "$PWD" -name "*".py)
echo $path
for i in $path
  do
    $(python $i)
    sleep 1m
  done

workdir=$(cd $(dirname $0); pwd)
echo $workdir
echo $0
#workdir=$(cd $(dirname $1); pwd)
#echo $workdir
#workdir=$(cd $(dirname $2); pwd)
#echo $workdir

$[$first_param + 1] &> /null
[ $? -ne 0 ] && printf "param must be number!" && exit

if [ 1 ==  $[$first_param+1] ]
then
#    echo "its ok"
    printf "its ok"
  else
    echo "its not ok"
    exit 2
fi
read -p "请输入第二个参数: " second_param;
read -p "请输入第三个参数: " thrid_param;

#for i
#do
# echo this is $i
#done

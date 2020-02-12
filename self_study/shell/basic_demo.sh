#!/bin/bash
str="test demo"
echo "this is $str"

# readonly 代表该变量为只读，不能改变
readonly str
#str="first change"
# 下面这种格式是多行注释
:<<EOF
  echo "test"
EOF

for skill in Ada Coffe Action Java
  do
    echo "I am good at ${skill}Script"
  done

for line in "This is a string"
  do
    echo "this is: ${line}"
  done

for i in {1..5}
  do
    echo "this is $i"
  done

for i in $(seq 5)
  do
    echo "this is $i"
  done

for i in $(seq 5 -1 1)
  do
    echo "this is $i"
  done

for((i=1;i<=5;i++))
  do
    echo "这是第 $i 次调用";
  done;
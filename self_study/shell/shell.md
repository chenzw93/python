### 	shell脚本学习总结点

1. #### 查看脚本执行过程： bash -x xxx.sh

2. #### 变量引用：

   1. 定义的变量，引用时使用 $开头

      ```shell
      str="test demo"
      echo "this is $str"
      ```

   2. 一般使用 双引号 教靠谱，如果使用 单引号 ，会出现问题

3. #### 循环

   1. for循环：

      - 有循环列表的循环：

        1.  `for i in {1..5};do echo this is $i;done;`打印1 2 3 4 5
        2. `for i in $(seq 5);do echo this is $i; done;` 打印1 2 3 4 5
        3. `for i in $(seq 5 -1 1);do echo this is $i;done `打印5 4 3 2 1
        4. `for i in {1..5..2};do echo this is $i;done`打印1 3 5

      - 无循环列表

        1. 循环次数为参数获取法

           ```shell
           #!/bin/env bash
           for i
           do
            echo this is $i
           done
           
           # 执行bash -x xx.sh
           $ bash -x test.sh a
           for i in '"$@"'
            echo this is a
            # 结果如下
           this is a
           ```

           执行脚本时，传递的参数都会作为循环时的变量，

      - 类C式循环: 固定写法`for((变量1;变量判断条件;变量执行操作))`

        ```shell
        for((i=1;i<5;i++));do echo $i;done; # 1 2 3 4
        ```


4. #### 运算符

   ​	只支持整数运算，不支持小数，如果想进行小数运算，可以如格式`echo 1+1.5|bc`

   * `$(())` : `echo $((1=1))`
   * `$[]`: `echo $[1+1]`
   * `expr`: `expr 1 \* 2` 运算符前后必须加空格
   * `let`: `let n=2**3;echo $n` 将2的三次方的值赋值给n

5. #### i++ 和++i区别

   * 对变量值来说，两者都是相同的
   * 对表达式来说，前者先复制，后++；后者先++，再赋值

6. #### 条件判断

   * `test 1==1`
   * `[ 表达式 ]`
   * `[[ 表达式 ]]`

7. #### 常用命令

   * `>` 输出，将内容重定向到`>`后的文件
   * `&>`输出，不管异常或正常，都重定向到`>`后的文件
   * `&&` 代表前面执行成功时，执行`&&`后面的操作
   * `||` 代表前面执行失败时，执行`||`后面的操作

8. #### 内置变量

   * `current_path="$PWD"` 获取当前目录
   * `parent_path=$(dirname "$PWD")`获取当前目录的父目录

9. #### `awk`关键字

   处理文本，`awk 动作 文件名`       

    [基本简介](http://www.ruanyifeng.com/blog/2018/11/awk.html)    [常用命令](https://www.cnblogs.com/xialiaoliao0911/p/7523982.html)

   * ```shell
     $ echo 'this is a test' | awk '{print $0}'
     this is a test
     ```

     > `$0`代表当前行
     >
     > `$1`,`$2`,`$3`: 代表第几个字段，如下
     >
     > ```shell
     > echo 'this is a test' | awk '{print $1}'  # this
     > ```
     >
     > `-F`参数： 后边跟分隔符
     >
     > ```shell
     > cat file
     > 1 1 1 a
     > 2 2 2 a
     > 3 3 3 a 
     > 4 4 4 4
     > 
     > $ cat file | awk -F " " '{print $1}' 
     > 1
     > 2
     > 3
     > 4
     > $ cat file | awk -F " " '/a/ {print $1}'
     > 1
     > 2
     > 3
     > ```

     > 其中`/a/` 代表正则式，`//`中间添加正则表达式，表示包含 a 的行

10. 
[TOC]

#### 1. 内置函数、作用域:

##### * isinstance(obj,type)

```python
isinstance("aaa",str)
# True
```

##### [变量作用域](https://www.runoob.com/python3/python3-namespace-scope.html)

1. built-in: Python内置变量。

2. global: module内定义的全局变量。

3. local: 函数内的变量。 global x 可以在local中直接使用、赋值global的变量

4. enclousure： 封装。即函数内可以再定义函数，跟外层是一样的。nonlocal x 同上

#### 2. 参数类型：

##### * 字符串(str)

[参照链接](https://www.runoob.com/python3/python3-string.html)

* [ : : ]
* 格式化

##### * 列表 [list]

操作包括 **索引，切片，加，乘**，检查成员

```python
lists = [11,22,33,44,55]
```

###### * 基本操作

* 获取

  > ```python
  > print(lists[2]) # 22
  > print(lists[1:3]) # [22,33]
  > ```

* 修改

  * 修改已有的值

  > ```python
  > lists[2] = 222
  > print(lists) # [11,222,33,44,55]
  > 
  > ```

  * 新添加

  > ```python
  > lists.append(666)
  > print(lists) # [11,222,33,44,55,666]
  > lists.insert(2, 777)
  > print(lists) # [11, 222, 777, 33, 44, 55, 666]
  > ```

* 删除

  * `del lists[<index>]` 删除某个索引处的元素
  * `lists.remove(<element>)` 删除指定元素
  * `lists.pop()` 删除最后一个元素

###### * 常用操作

`lists = ["a","b","c","d","e","f","g"]`

|  `[1,2,3] + [4,5,6]`   |     `[1,2,3,4,5,6]`     |                         `+` 列表合并                         |
| :--------------------: | :---------------------: | :----------------------------------------------------------: |
|                        |                         |                                                              |
|      `["a"] * 5`       | `["a","a","a","a","a"]` |                         `*` 内容复制                         |
| `"a" in ["a","b","c"]` |         `True`          |                      `in` 判断是否存在                       |
|      `lists[-1]`       |           `g`           |                     `[-index]` 反向获取                      |
|    `lists[1:10:2]`     |    `['b', 'd', 'f']`    |                    `[start : end: step]`                     |
|    `lists[-5:-1:1]`    | `['c', 'd', 'e', 'f']`  | start: 第一个元素起始；end：最后一个元素截止；step: 索引增加的步长 |

###### * 方法

* `list(seq)`: 元祖转成列表
* `max(list)`: 元素中最大值
* `min(list)`: 元素中最小值
* `list.extend(seq)`: 拼接列表
* `list.count(obj)`: 查找obj在列表中的个数
* `list.reverse()`: 列表翻转，原始列表变为反序
* `list.sort()`: 列表排序
* `list.copy()`: 列表复制; copy一份数据
* `list.index(obj)`:  查询元素在列表中的索引

##### * 元组 (tuple)

​	基本操作同 **列表**，但是没有任何修改的操作，因为是不可变数据

> 如果只有一个元素，不能用**`(a)`**表示，正确表示为**`(a,)`**

* `tuple(seq)` : 转成元组 

##### * 字典 {dict}

**形式：**`{key:value,key1:value1}`

**说明：**键必须是唯一的，但值则不必。值可以取任何数据类型，但键必须是不可变的，如字符串，数字或元组

###### * 常用操作

* `get(key, "default")` : 如果key不存在，则返回default，如果default为空，则返回None

* [参考链接](https://www.runoob.com/python3/python3-dictionary.html)

##### * 集合(set)

是一个无序的不重复元素序列，可以使用大括号 **{ }** 或者 **set()** 函数创建集合，注意：创建一个空集合必须用 **set()** 而不是 **{ }**，因为 **{ }** 是用来创建一个空字典

###### * 常用操作

* 添加
  * `add()`
  * `update()` 可以是 列表，元组，字典
* 删除
  * `remove(obj)` 如果元素不存在，则会发生错误。
  * `discard(obj)`  如果元素不存在，不会报错
  * `pop()` 随机删除一个元素
* [参考链接](https://www.runoob.com/python3/python3-set.html)

#### 3. 函数参数:

##### * 可变类型、不可变类型

* 在 python 中，`strings` , `tuples `, 和 `numbers` 是不可更改的对象，而 `list` ,`dict` ,`set`等则是可以修改的对象。

* 声明函数时，参数中星号 **`*`** 可以单独出现，但是如果单独出现**`*`** 后的参数必须用关键字传入

  ```python
  def func(a,b,*,c):
      print(a,b,c)
  
  func(10,20,c=30) # 10 20 30
  func(10,20,30) # TypeError: func() takes 2 positional arguments but 3 were given
  
  def func1(a, b, *args, **c):
      print(a, b)
      print(args)
      print(c)
  
  
  func1(10, 20, 30, 40, name="xiaohua", age=18)
  # 10 20
  # (30, 40)
  # {'name': 'xiaohua', 'age': 18}
  ```

> - **不可变类型： 传递副本给函数，函数内操作不影响原始值；**变量赋值 **a=5** 后再赋值 **a=10**，这里实际是新生成一个 int 值对象 10，再让 a 指向它，而 5 被丢弃，不是改变a的值，相当于新生成了a。
> - **可变类型：传递地址引用，函数内操作可能会影响原值**变量赋值 **la=[1,2,3,4]** 后再赋值 **la[2]=5** 则是将 list la 的第三个元素值更改，本身la没有动，只是其内部的一部分值被修改了。
>
> python 函数的参数传递：
>
> - **不可变类型：**类似 c++ 的值传递，如 整数、字符串、元组。如fun（a），传递的只是a的值，没有影响a对象本身。比如在 fun（a）内部修改 a 的值，只是修改另一个复制的对象，不会影响 a 本身。
> - **可变类型：**类似 c++ 的引用传递，如 列表，字典。如 fun（la），则是将 la 真正的传过去，修改后fun外部的la也会受影响
>
> python 中一切都是对象，严格意义我们不能说值传递还是引用传递，我们应该说传不可变对象和传可变对象。

##### * 位置匹配

##### * 关键字参数

> ```python
> def func(name, age):
>     print(f"name： {name}, age: {age}")
> 
> func(name="xiaohua", age=20) # name： xiaohua, age: 20
> ```

##### * 默认值参数（调用时省略传值）

> ```python
> def func(name, age = 18):
>     print(f"name： {name}, age: {name}")
> 
> func(name="xiaohua")  # name： xiaohua, age: 18
> ```

##### * 不定长参数

`*` 开头的形参。`*args` 可以接收 [tuple] 类型的数据。示例如下：

```python
def fun_variable(*names):
    print(names)


names = ("xiaohua", "xiaobei")
if __name__ == '__main__':
    fun_variable(names)  # (('xiaohua', 'xiaobei'),)
    fun_variable(*names)  # ('xiaohua', 'xiaobei')
```

##### * 指定参数

`**` 开头的形参。`**kwargs` 可以接收 [dict] 类型的数据。示例如下：

```python
def fun_keyword(**student):
    print(student)

student = {"name": "xiaohua", "age": 18}
student_con = dict(name="xiaohua", age=18)
fun_keyword(name="xiaohua", age=18) # {'name': 'xiaohua', 'age': 18}
fun_keyword(**student) # {'name': 'xiaohua', 'age': 18}
fun_keyword(**student_con) # {'name': 'xiaohua', 'age': 18}
fun_keyword(student) # TypeError: fun_keyword() takes 0 positional arguments but 1 was given
```

#### 4. lambda

 表达式： `lambda param1,param2... : 函数`

#### 5. 高级工具

##### * map(操作函数, 待操作序列)：

```python
map(lambda x, y: x + y, [1, 3, 5, 7, 9], [2, 4, 6, 8, 10])
# [3,7,11,15,19]
```

##### * filter(操作函数,待操作序列)：

```python
filter(lambda x:x%2 ==0, range(11))
# <filter object at 0x00000000029B8D08>
list(filter(lambda x: x % 2 == 0, range(11)))
# [0, 2, 4, 6, 8, 10]
```

##### * reduce(操作函数,带操作序列): 

python3 后`reduce` 需要导入后使用

`from functools import reduce`

```python
from functools import reduce

reduce(lambda x, y: x+y, [1,2,3,4,5])
# 15
```
##### * sorted

**`sorted(_iterable,key,reverse)`**

> _iterable: 可迭代列表
>
> key ： 排序条件,一般为函数。可以使用lambda表达式，如str.lower等。如果按字符串排序，默认的是按ASCII排序，	即'Z' < 'a'
>
> reverse：是否反转

#### 6. 判断条件，循环

##### * if

```python
if <conditions>:
    <statement>
elif <conditions>:
    <statement>
else:
    <statement>
```

##### * for

```python
for <variable> in <sequence>:
    <statements>
else:
    <statements>
```

- `[x for x in range(11) if x % 2 == 0]`

- ```python
  [m + n for m in 'ABC' for n in 'XYZ']
  # ['AX', 'AY', 'AZ', 'BX', 'BY', 'BZ', 'CX', 'CY', 'CZ']
  ```

- ```python
  >>>a = ['Google', 'Baidu', 'Runoob', 'Taobao', 'QQ']
  >>> for i in range(len(a)):
  ...     print(i, a[i])
  ... 
  0 Google
  1 Baidu
  2 Runoob
  3 Taobao
  4 QQ
  >>>
  ```

##### * while

```python
while <conditions>:
    <statements>
else:
    <statements>
```

#### 7. 迭代器

#### 8. 生成器

[参考链接](https://www.runoob.com/python3/python3-iterator-generator.html)

`yield`关键字

#### 9. 面向对象

##### * 三大特性

###### * 封装：

> 构造函数，
>
> ```python
> def __init__(self,name):
>     self._name = name
> ```

###### * 继承

> ```python
> class Person:
>     def __init__(self, name):
>         self._name = name
> 
>     def eat(self):
>         print(f"{self._name} eat")
> 
> 
> class Teacher(Person):
>     def __init__(self, name, course):
>         super(Teacher, self).__init__(name)
>         self._course = course
> 
> 
> x = Teacher("xiaobei", "python")
> print(x.eat()) # xiaobei eat
> ```

* 支持多重继承

  ```python
  class Teacher(object, Person):
  ```

* 子类与父类相同方法时，会覆盖父类的方法

###### * 多态



##### * 成员变量

* Python 没有绝对的私有变量，一般约定

  * **`_`**代表保护变量，意思是只有类对象和子类对象自己能访问到这些变量；不能直接访问的类属性，需通过类提供的接口进行访问，不能用“from xxx import *”而导入
  * `__`代表私有变量，只有类对象自己能访问，连子类对象也不能访问到这个数据；

* getter/setter 方法获取成员变量

  ```python
  class Person:
      def __init__(self, name):
          self._name = name
  
      @property
      def name(self):
          return self._name
  
      @name.setter
      def name(self, name):
          self._name = name
  
      def eat(self):
          print(f"{self._name} eat")
  
          
  x = Person("xiaobei")
  print(x.name) # xiaobei 调用使用@property标记的方法获取值
  x.name = "xiaohua" # 调用setter方法进行赋值操作
  print(x.name) # xiaohua
  ```

* \__slots__

  如果类中没有该变量，可以动态给 对象、类添加成员变量，或者成员方法，可以通过`__slots__`强制

  ```python
  class Person：
  	__slots__ = ("name","age","course")
      
  # 成员变量只能为 name，age，course三个，不能动态添加成员变量
  ```

##### * 对象常用函数

###### * `__str__(self)`

```python
    def __str__(self):
        return f"{self.name} teach {self._course} -> __str__"
```

###### * `__repr__(self)`

```python
    def __repr__(self):
        return f"{self.name} teach {self._course} -> __repr__"
```

###### * [`__getattr__`](https://www.liaoxuefeng.com/wiki/1016959663602400/1017590712115904)

##### * [参考链接](https://www.liaoxuefeng.com/wiki/1016959663602400/1017590712115904)

##### * 枚举类

* ```python
  from enum import Enum
  
  Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
  
  # Jan => Month.Jan , 1
  # Feb => Month.Feb , 2
  # Mar => Month.Mar , 3
  # ...
  ```

* ```python
  from enum import Enum, unique
  
  @unique
  class WEEK(Enum):
      SUN = 0
      MON = 1
      THU = 2
      FRI = 3
  
  # print(WEEK.MON, WEEK.MON.value)
  # print(WEEK(3))
  ```

#### 10. [内置模块函数](https://www.runoob.com/python3/python3-stdlib.html)

##### * os

* **`os.environ.get(key)`** : 获取环境变量
* **`os.listdir(path) `** : 获取`path`目录下文件，目录列表
* **`os.walk(path,topdown=True, onerror=None, followlinks=False)`** : 获取`path`下所有的目录，文件列表。返回值为root，dirs, files
* **`os.path.join(path, *paths)`**:  path拼接
* **`os.path.split(path)`**:  返回路径的最后一级文件或者文件夹的名称和前边的路径
* **`os.path.splitext(path)`**： 返回文件扩展名

```python
import os

def get_files(file_path):
    # os.listdir 查询当前目录下所有目录，文件，不包含子目录
    for x in os.listdir(file_path):
        # os.path.join 目录拼接
        file = os.path.join(file_path, x)
        # os.path.isfile 判断是文件还是文件夹
        if os.path.isfile(file):
            print(file)
        else:
            get_files(file)
            
for root, dirs, files in os.walk(current_dir):
    print(root) # 当前目录地址
    print(dirs) # 当前目录地址下的文件夹
    print(files) # 当前目录地址下的文件
```

##### * sys

```python
import sys

print(sys.argv) # 获取执行命名参数列表，第一个为脚本文件名称
```

##### * [datetime](https://blog.csdn.net/qq_41805715/article/details/100070706)

`from datetime import date`

`from datetime import datetime`

##### * 正则

```python
import re
```

* 匹配字符串

  直接使用`re.match(reg,str)`即可。`compile`: 编译正则表达式，生成一个正则表达式对象； 

  ```python
  import re
  
  input_line = "this is a line"
  if re.match(r"^[a-zA-Z\s]+$", input_line):
      print("input is ok")
  else:
      print("input is error")
  # input is ok    
  
  input_line = "this is a line"
  input_re = re.compile(r"^[a-zA-Z\s]+$")
  if input_re.match(input_line):
      print("input is ok")
  else:
      print("input is error")
  # input is ok
  ```

* 分组：提取字符串

  ```python
  m = re.match(r'^(\d{3})--(\d{3,8})$', '010--12345')
  print(m)
  print(m.groups())
  print(m.group(0))
  print(m.group(1))
  print(m.group(2))
  
  # <re.Match object; span=(0, 10), match='010--12345'>
  # ('010', '12345')
  # 010--12345
  # 010
  # 12345
  ```

##### * 数据压缩

* zlib

* gzip

* tarfile

* zipfile

  ```python
  import zipfile
  
  def zip_file(src, dist):
      with zipfile.ZipFile(dist, 'w') as zip_io:
          for root, dirs, files in os.walk(src):
              for file in files:
                  zip_io.write(os.path.join(root, file))
  
                  
  zip_file("./", "./demo1.zip")
  ```

  

##### * shutil

* shutil.copy()
* shutil.move()

##### * glob

通配符搜索对应的文件列表

* glob.glob('*.py')

#### 11. 异常

##### * 结构

```python
try:
    xxx
except:
 	xxx
else:
    xxx # 如果没有抛出异常，会执行
finally:
    xxx
    
try:
    print('try...')
    r = 10 / int('2')
    print('result:', r)
except ValueError as e:
    print('ValueError:', e)
except ZeroDivisionError as e:
    print('ZeroDivisionError:',e)
else:
    print('no error!')
finally:
    print('finally...')
```

##### * 异常

Python所有的错误都是从 **`BaseException`** 类派生的

[官方文档](https://docs.python.org/3/library/exceptions.html#exception-hierarchy)

##### * `raise`

* 如果不带异常类型，会将换异常抛出
* 如果代理异常类型，则抛出对应的异常类型

#### 12. IO

##### * 函数

`open(file, mode='r', buffering=None, encoding=None, errors=None, newline=None, closefd=True)`

##### * 常见使用

* ```python
  with open("a.txt",mode='r',encoding='utf-8') as input:
      input.readline() # 读取一行
      input.readlines() # 按行读取所有内容
      input.read(nums) # 读取指定的字节数
  ```

* ```python
  with open("a.txt",mode='w',encoding='utf-8') as output:
      output.write("content") #
      output.writelines(list) #
  ```

##### *pickle

```python
import pickle
 
pickle.dumps(data) # 数据序列化
pickle.dump(data, output) # 将data序列化后写入output对应的文件 output = open(file)
pickle.load(input) # 将序列化的文件内容加载到内存中，input = open(file)
```

##### * JSON

```python
import json

json.dumps(data) # 数据转成json数据
json.dump(data, output) # 数据转成json数据存储到output对应的文件 output = open(file)
json.load(data,input) # 从input对应的文件读取数据
json.loads(data) # 数据序列化
```

* 普通对象转JSON

  ```python
  import json
  
  class Student(object):
      def __init__(self, name, age, score):
          self.name = name
          self.age = age
          self.score = score
          
     	def student2dict(std):
          return {
              'name': std.name,
              'age': std.age,
              'score': std.score
          }
      
  s = Student('Bob', 20, 88)
  json.dumps(s, default=Student.student2dict) # {"age": 20, "name": "Bob", "score": 88}
  json.dumps(s, default=lambda obj: obj.__dict__) # {"name": "Bob", "age": 20, "score": 88}
  ```

  
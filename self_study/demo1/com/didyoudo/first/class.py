"""
    1. 成员变量等
        1.1 私有变量: __ 双下划线开头的变量。 但是Python中没有绝对的私有变量，约定俗称
        1.2 特殊变量: __xxx__ 双下划线开头、结尾
    2. 构造函数
    3. 继承
    4. 多态
    常用的方法：
        type(): 判断变量的类型
        isinstance():
        dir():
        getattr()、setattr()以及hasattr():
    5. 属性： __slots__ 定义该类中允许定义的成员变量，而且只作用于该类的对象，子类的对象无效

"""


# 请利用@property给一个Screen对象加上width和height属性，以及一个只读属性resolution：
class Screen:

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, width):
        self._width = width

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, height):
        self._height = height

    @property
    def resolution(self):
        return 786432


s = Screen()
s.width = 1024
s.height = 768
print(s.width)
print(s.height)
print('resolution =', s.resolution)
if s.resolution == 786432:
    print('测试通过!')
else:
    print('测试失败!')

#
# print(type(111) == int)
# print(isinstance(111, int))
#
#
# class Animal:
#     __slots__ = 'name'
#
#     def __init__(self, name):
#         self.name = name
#
#     # def __init__(self, name, age):
#     #     self.name = name
#     #     self.age = age
#
#     def eat(self):
#         print(f"{self.name}  need eat ")
#
#     def sleep(self):
#         print("animal need sleeping")
#
#
# # print(dir(Animal))
# animal = Animal();
# animal.address = "aaa"
# print(animal.address)
# Animal.address = "aaa";
# print(Animal.address)
#
#
# class Pig(Animal):
#     pass
#
#
# class Dog(Animal):
#     pass
#
# small_pig = Pig("small_pig")
# small_pig.eat()
#
# small_dog = Dog("small_dog")
# small_dog.eat();

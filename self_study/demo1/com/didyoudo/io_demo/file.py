import logging

logging.basicConfig(level=logging.INFO)


def func(name, age):
    print(f"name： {name}, age: {age}")


def func(name, age=18):
    print(f"name： {name}, age: {age}")


def func1(a, b, *args, **c):
    print(a, b)
    print(args)
    print(c)


def update_lists(names):
    names[0] = "a"
    print(names)


def update_tuples(names):
    names.get()


# lists = [1, 2, 3]
# print(lists)
# update_lists(lists.copy())
# update_lists(lists[:])
# print(lists)

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


class Teacher:
    __slots__ = ("name", "course")

    # def __init__(self, name, course):
    #     super(Teacher, self).__init__(name)
    #     self._course = course
    #
    # def __str__(self):
    #     return f"{self.name} teach {self._course} -> __str__"
    #
    # def __repr__(self):
    #     return f"{self.name} teach {self._course} -> __repr__"


# x = Teacher("xiaobei", "python")
x = Teacher()
# print(x.eat())
print(x)
x.name = "sss"
print(x.name)
x.name = "xiaohua"
print(x.name)
x.age = 10
print(x.age)
x.walk = lambda x: print(f"{x} is walking")
x.walk("xiaohua")
# tuples = (1, 2, 3)
# print(tuples)
# update_lists(tuples)
# print(tuples)

# func1(10, 20, 30, 40, name="xiaohua", age=18)

# func(name="xiaohua", age=20)
# func(name="xiaohua")
#
# print(list(filter(lambda x: x % 2 == 0, range(11))))
# print([x for x in range(11) if x % 2 == 0])
# for x in range(11):
#     print(x)
# print(range(11))


# 1.1 read -> ordinary
# try:
#     f = open("F:/aaa.txt", "r")
#     for line in f.readlines():
#         logging.info(f"content: {line}")
#
# finally:
#     logging.info("finally")
#     if f:
#         logging.info(f)
#         f.close()

# 1.2 read -> with
# with open("F:/aaa.txt", "r") as file:
#     for line in file.readlines():
#         logging.info(f"content: {line.strip()}")  # 把末尾的'\n'删掉

# 2.2 write -> with
# content = ["its first", "its second", "end"]
# with open("F:/aaa.txt", "a") as file:
#     for line in content:
#         logging.info(f"{line}")
#         file.writelines(line)

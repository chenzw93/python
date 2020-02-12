from enum import Enum, unique


@unique
class WEEK_DAY(Enum):
    Sun = 0  # Sun的value被设定为0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6


print(WEEK_DAY.Sun)
print(WEEK_DAY.Sun.value)
print(WEEK_DAY.Sun.name)


# @unique
class Gender(Enum):
    Male = 0
    Female = 1


class Student:
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

    def __str__(self):
        return f"student name {self.name}"


bart = Student('Bart', Gender.Male)
print(bart)
if bart.gender == Gender.Male:
    print('测试通过!')
else:
    print('测试失败!')


def demo_test(num):
    try:
        a = 10 / num
    except Exception as b:
        print(f"zero exception, num: {num}")
    else:
        print("its ok")


demo_test(0)
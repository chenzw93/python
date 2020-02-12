class Student:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def __str__(self):
        print("student: name={},age={}".format(self._name, self._age))
        print("student: name=%s,age=%s" % (self._name, self._age))
        return f"student: name={self._name}, age={self._age}"


def main():
    student = Student("xiaoxi", 18)
    print(student)


if __name__ == '__main__':
    main()
    flag0 = 1 == 1
    flag1 = 3 > 2
    flag2 = 2 < 1
    flag3 = flag1 and flag2
    flag4 = flag1 or flag2
    flag5 = not (1 != 2)
    print('flag0 =', flag0)  # flag0 = True
    print('flag1 =', flag1)  # flag1 = True
    print('flag2 =', flag2)  # flag2 = False
    print('flag3 =', flag3)  # flag3 = False
    print('flag4 =', flag4)  # flag4 = True
    print('flag5 =', flag5)  # flag5 = False
    print(flag1 is True)  # True
    print(flag2 is not False)  # False

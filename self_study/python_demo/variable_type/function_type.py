def fun_variable(*names):
    print(names)


def fun_keyword(**student):
    print(student)


names = ("xiaohua", "xiaobei")
student = {"name": "xiaohua", "age": 18}
student_con = dict(name="xiaohua", age=18)


def lambda_fun(args):
    print("args: ", args)


lists = list(range(1, 11))

if __name__ == '__main__':
    print([x for x in lists if x % 2 == 0])
    print(list(filter((lambda var: var % 2 == 0), lists)))
    tup1 = ('physics', 'chemistry', 1997, 2000)
    tup2 = (1, 2, 3, 4, 5, 6, 7)

    print ("tup1[0]: ", tup1[0])
    print ("tup2[1:5]: ", tup2[1:5])
    # fun_variable(names)  # (('xiaohua', 'xiaobei'),)
    # fun_variable(*names)  # ('xiaohua', 'xiaobei')
    # fun_keyword(student)
    # fun_keyword(name="xiaohua", age=18)
    # fun_keyword(**student)
    # fun_keyword(**student_con)
    # lambda_fun("xiaobei")
    # (lambda args: print(args))("xiaobei")

# 1. max min
# maxValue = max(0,2,34,123,312,3)
# print(maxValue)
# minValue = min(1.2,342,423,4,1)
# print(minValue)

# 2. abs 绝对值函数
# print(abs(-123))

# 3. 类型转换
# print(int('123'))
# print(int(123.10))
# print(bool(''))
# print(bool(11))
#
# print(hex(10))
# print(format(10, '#X'))
# print('%#X' % 10)

# 4. 默认参数的函数
'''
默认参数要指向不可变对象
'''

# def test_func(list = []):
#     list.append("end");
#     return list;
#
# test_func()
# test_func()
# print(test_func()) # ["end","end","end"]


# 5. 可变参数
# def test_variable(*names):
#     '''
#      参数前加 * 即可，集合或元组数据也可加 * 转变成可变参数传递
#     :param names:
#     :return:
#     '''
#     for name in names:
#         print(f"hello: {name}")
#
# test_variable()
# print("=====================")
# test_variable("xiaobei", "xiaohua", "xiaohei")
# print("=====================")
# names = ["xiaobei", "xiaohua", "xiaohei"]
# test_variable(*names)

# 6. 关键字参数   关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict
# def test_key(name, age, **other):
#     print(f"name: {name}, age: {age}, other: {other}")
#
#
# test_key("xiaohua", 10)  # name: xiaohua, age: 10, other: {}
# test_key("xiaohua", 10, address="hebei", phone=110)  # name: xiaohua, age: 10, other: {'address': 'hebei', 'phone': 110}
# test_key("xiaohei", 27,
#          **{"address": "hebei", "phone": 110})  # name: xiaohei, age: 27, other: {'address': 'hebei', 'phone': 110}

# 7. 命名关键字  用 * 分开参数，指定参数名称
# def test_name_key(name, age, *, address, phone):
#     print(f"name: {name}, age: {age}, address: {address}， phone: {phone}")
#
#
# test_name_key("xiaobai", 15, address="beijing",
#               phone=13123123123)  # name: xiaobai, age: 15, address: beijing， phone: 13123123123


'''
    参数分类：
        必选参数： 普通传参
        默认值参数： 可以提前给参数赋值即 param = value
        可变参数： 以 * 开头，可以为0或多个参数，*args 函数中是以tuple接收 ()
        命名关键字参数： 用 * 隔开，后面指定参数的名称 param1, *, param2, param3; 如果前边是可变参数，可以省略 * 
        关键字参数： 以 ** 开头，可以表示0个或多个参数， **keys 函数中以dict接收{}
        
        函数中的参数位置，从上到下依次为从前到后
'''


def consolution_function(param1, param2, *args, param3, param4, **keys):
    print(f"param1: {param1}, param2: {param2}, args: {args}, param3: {param3}, param4: {param4}, keys: {keys}")


# param1: xiaohua, param2: 10, args: ('xiaowa', 'xiaobai'), param3: param3, param4: param4, keys: {'address': 'beijing'}
consolution_function("xiaohua", 10, "xiaowa", "xiaobai", param3="param3", param4="param4", **{"address": "beijing"})

'''
数据类型
    整数
    浮点数
    字符串
    list
    tuple
    dict
    set
    1. set、dict 只能是不可变类型数据，{}
    2. tuple 即为数组，元素个数确定  ()
    3. list 可变集合 []
条件判断：
    if 条件：执行语句
    if 条件： 执行语句 elif 条件： 执行语句 else：执行语句
循环：
    while
    for xxx in xxx
    continue
    break
'''
# name = 10
# print(name)
#
# name = 1.1
# print(name)
#
# name = 'dd'
# print(name)
#
# print('''ffff
# ...dddd
# ...aaa''')
#
# print('fff\\')
# print(r'fff\\')
#
# print('%2d-%02d' % (3, 1))
# print('%.2f' % 3.1415926)
#
# s1 = 72
# s2 = 85
# r = (s2 -s1) / s1 * 100
# print(r)
# print('%.1f%%' % r)

'''
    list features:
        1. 元素类型可以不一致，可以嵌套list
        2. 
'''
# lists = [111, 222, 333]
# len(lists)
# print(lists[0])
# print(lists[-1])
# print(lists)
# lists.pop(0);
# print(lists)
#
# names = ['Bart', 'Lisa', 'Adam']
# for name in names:
#     print('hello, %s!' % name)

'''
    tuple
        元素的指向永不变，同时元素类型可以多种，嵌套list等，
'''
# tuples = ()

'''
    dict(dictionary): 字典，即map，键值对
'''
# dicts = {'name':"xiaobei","age": 1,"address":"baoji",10:'age'}
# print(dicts.get('names') is None)
# print(dicts.get(10) is None)
# print(dicts['name'])
# # print(dicts['names'])
# print(dicts[10])

'''
    set
'''
# sets = set((1, 2, 3))
# print(sets)
# print(type(sets))

'''
    if : xxx elif: xxx 
'''
# age = 10
# if age == 10 :
#         print("age > 10")
#         print("age <= 10")
#
# birth = int(input('birth: '))
# if birth > 2000 :
#     print("age <= 20")
# else:
#     print("age > 20")
from collections.abc import Iterable

'''
    map 遍历：
        key： for key in dicts:
        value： for value in dicts.values():
        key and value： for key, value in dicts.items():
        
    list 实现普通索引遍历：
        关键字 enumerate
        for index, value in enumerate(['A', 'B', 'C']):
'''

#dicts = {"name":"xiaohua", "age": 10, "address": "basailuona"}
# 遍历key
# for key in dicts:
#     print(f"key: {key}")
#
# # 遍历value
# for value in dicts.values():
#     print(f"value: {value}")
#
# # 遍历key，value
# for key,value in dicts.items():
#     print(f"key: {key} = value: {value}")

# 索引遍历
for index, value in enumerate(['A', 'B', 'C']):
    print(f"index: {index} -> value: {value}")

# 判断是否可以迭代
print(isinstance("aaaa", Iterable))
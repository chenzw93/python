# 双层循环   ['AX', 'AY', 'AZ', 'BX', 'BY', 'BZ', 'CX', 'CY', 'CZ']
print([m + n for m in 'ABC' for n in 'XYZ'])

# 生成偶数集合
"""
    range(1, 11) 代表生成[1,11)直接的整数
"""
print(list(range(1, 11)))  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print([x * x for x in range(1, 11)])  # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
print([x * x for x in range(1, 11) if x % 2 == 0])  # [4, 16, 36, 64, 100]

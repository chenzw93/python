"""
    集合、字符串等可以使用切片，获取某个元素
    [起始索引 : 结束索引 : 步长]
    起始索引： 从该索引位置起获取元素
    结束索引： 到该索引位置，不包含该索引处的元素
    步长: 获取元素时，从起始索引间隔几进行获取，默认为1
    注意：
        其中索引可以为负数，此时从后往前取
"""
print("abcdefg"[0:3])  # abc
print("abcdefg"[0:5:2])  # ace
print(["aaa", "bbb", "ccc"][0:2])  # ['aaa', 'bbb']
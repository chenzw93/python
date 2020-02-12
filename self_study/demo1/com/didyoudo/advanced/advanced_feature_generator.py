"""
    生成器：
        第一种： 将生成式的 [] 换成 () 即可，
        第二种： 函数变为生成器，函数中包含关键字 yield
"""
# lists = [x * x for x in range(1, 11)]
# print(lists)
# generator = (x * x for x in range(1, 11))
# print(generator)
# print(next(generator))
# print(next(generator))
# print(next(generator))
# print(next(generator))
# print(next(generator))
# print(next(generator))
# print(next(generator))
# print(next(generator))
# print(next(generator))
# print(next(generator))
# print(next(generator))
# for x in generator:
#     print(x)


# 普通斐波拉切数列
# def normal_fibonacci_sequence(length):
#     n, pre, next = 0, 0, 1
#     while n < length:
#         print(next)
#         pre, next = next, pre + next
#         n = n + 1
#     return 'done'
#
# normal_fibonacci_sequence(6)

# 生成器 斐波拉切
# def normal_fibonacci_sequence(length):
#     n, pre, next = 0, 0, 1
#     while n < length:
#         yield next  # 主要区别在于这个地方的yield
#         pre, next = next, pre + next
#         n = n + 1
#     return 'done'
#
# for x in normal_fibonacci_sequence(10):
#     print(x)

# 杨辉三角
from typing import List

"""
          1
         / \
        1   1
       / \ / \
      1   2   1
     / \ / \ / \
    1   3   3   1
   / \ / \ / \ / \
  1   4   6   4   1
 / \ / \ / \ / \ / \
1   5   10  10  5   1
"""
# 实例化一个6个元素的集合
# row = [None for i in range(5 + 1)]
# print(row)


# def generate(num_rows):
#     triangle = []
#
#     for row_num in range(num_rows):
#         # The first and last row elements are always 1.
#         row = [None for _ in range(row_num + 1)]
#         row[0], row[-1] = 1, 1
#
#         # Each triangle element is equal to the sum of the elements
#         # above-and-to-the-left and above-and-to-the-right.
#         for j in range(1, len(row) - 1):
#             row[j] = triangle[row_num - 1][j - 1] + triangle[row_num - 1][j]
#
#         triangle.append(row)
#
#     return triangle
#
# print(generate(5))

def generate( numRows: int) -> List[List[int]]:
        triangle = []

        for row_num in range(numRows):
            # The first and last row elements are always 1.
            row = [None for _ in range(row_num + 1)]
            row[0], row[-1] = 1, 1

            # Each triangle element is equal to the sum of the elements
            # above-and-to-the-left and above-and-to-the-right.
            for j in range(1, len(row) - 1):
                row[j] = triangle[row_num - 1][j - 1] + triangle[row_num - 1][j]

            triangle.append(row)

        return triangle


print(generate(numRows=5))
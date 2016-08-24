# -*- coding: utf-8 -*-
from utility import array_utility as au


# 归并过程 ,这种过程得益于有切片功能，和数组操作极其方便的 python语言设计。所以这种实现方式，基本只会在python中出现
def merge(left_array, right_array):
    right, left = 0, 0
    result = []
    left_array_length = len(left_array)
    right_array_length = len(right_array)
    while left < left_array_length and right < right_array_length:
        if left_array[left] < right_array[right]:
            result.append(left_array[left])  # [4,3] [1,6] 如果 4 < 1 则把4添加进临时数组
            left += 1
        else:
            result.append(right_array[right])  # [4,3] [1,6] 不然 就把 1添加进临时数组
            right += 1
    result += right_array[right:]  # 把剩余条目扔进result中
    result += left_array[left:]  # 把剩余条目扔进result中
    return result


# 归并排序 ，开局就是递归，递归，递归... 一直到数组中就两个元素拿去归并。[4,3] [1,6] 会归并成 [1,3,4,6]以此为返回结果，弹栈继续递归，
# 以[1,3,4,6]为一个单位与另一个单位继续归并，一次类推，返回结果.
def merge_sort(array):
    if len(array) <= 1:
        return array
    middle = int(len(array) / 2)
    left_array = merge_sort(array[:middle])
    right_array = merge_sort(array[middle:])
    return merge(left_array, right_array)


if __name__ == "__main__":
    temp_array = au.generate_array()
    print(temp_array)
    temp_array = merge_sort(temp_array)
    print(temp_array)

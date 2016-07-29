# -*- coding: utf-8 -*-
from utility import array_utility as au


# 通过下标的形式进行归并排序,开始用[None]初始化数组的时候，调用Append方法，插入了None的后面。。。蛋疼
def merge(array, low, middle, high):
    temp = [None] * (high - low + 1)
    left = low
    right = middle + 1
    cursor = 0

    while left <= middle and right <= high:
        if array[left] < array[right]:
            temp[cursor] = array[left]
            left += 1
        else:
            temp[cursor] = array[right]
            right += 1
        cursor += 1

    while left <= middle:
        temp[cursor] = array[left]
        cursor += 1
        left += 1

    while right <= high:
        temp[cursor] = array[right]
        cursor += 1
        right += 1

    for migrate in range(0, len(temp)):
        array[low + migrate] = temp[migrate]


def merge_sort(array, low, high):
    middle = int((high + low) / 2)
    if low < high:
        merge_sort(array, low, middle)
        merge_sort(array, middle + 1, high)
        merge(array, low, middle, high)


if __name__ == "__main__":
    temp_array = au.generate_array()
    print(temp_array)
    merge_sort(temp_array, 0, len(temp_array) - 1)
    print(temp_array)

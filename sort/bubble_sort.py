# -*- coding: utf-8 -*-
from utility import array_utility as au


# 冒泡排序  执行的对比次数为：(n*(n-1))/2   平均执行交换次数是对比次数的50% 也就是 (n*(n-1))/4 最坏情况为  ((n*n-1)/2) * ((n*n-1)/2) 时间复杂度为O(n²)
def bubble_sort(array):
    for outer in range(0, len(array)):
        for inner in range(0, (len(array) - outer) - 1):
            if array[inner] > array[inner + 1]:
                au.exchange(array, inner, inner + 1)


if __name__ == "__main__":
    temp_array = au.generate_array()
    print(temp_array)
    bubble_sort(temp_array)
    print(temp_array)

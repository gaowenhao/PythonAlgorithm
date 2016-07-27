# -*- coding: utf-8 -*-
from utility import array_utility as au


# 插入排序相对冒泡排序和选择排序，减少了一定的对比次数，但是交换次数并没有减少 时间复杂度 同为O(n²)
def select_sort(array):
    for outer in range(1, len(array)):
        inner = outer
        temp = array[inner]
        while inner > 0 and array[inner-1] > temp:
            array[inner] = array[inner - 1]
            inner -= 1
        array[inner] = temp


if __name__ == "__main__":
    temp_array = au.generate_array()
    print(temp_array)
    select_sort(temp_array)
    print(temp_array)

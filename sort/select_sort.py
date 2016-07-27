# -*- coding: utf-8 -*-
from utility import array_utility as au


# 选择排序 每个外部循环会计算出最小的值 ，需要比较的次数为 (n*(n-1)) / 2 需要交换的次数相对冒泡排序少了一些 ，时间复杂度还是O(n²)
def select_sort(array):
    for outer in range(0, len(array)):
        for inner in range(outer + 1, len(array)):
            if array[outer] > array[inner]:
                au.exchange(array, outer, inner)


if __name__ == "__main__":
    temp_array = au.generate_array()
    print(temp_array)
    select_sort(temp_array)
    print(temp_array)

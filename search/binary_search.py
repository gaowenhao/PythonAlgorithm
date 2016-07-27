# -*- coding: utf-8 -*-
from utility import array_utility as au


# 循环的方式进行二分查找 时间复杂度为O(log2n)
def binary_search(array, key):
    low = 0
    high = len(array) - 1
    while low < high:
        middle = int((high - low) / 2)
        if array[middle] > key:
            low = middle + 1
        elif array[middle] < key:
            high = middle
        else:
            return middle


if __name__ == "__main__":
    temp_array = sorted(au.generate_array(30))
    result = binary_search(temp_array, temp_array[7])
    print(result)

# -*- coding: utf-8 -*-
from utility import array_utility as au


# 快速排序 每次选出一个数temp，遍历数组两头，右指针发现比他小的，左指针发现比他大的。
# 当左右各发现一个数值的时候，把这两个数值交换，以此类推。最后把temp挪到中间，重复这个过程。
# 时间复杂度为 O(log2n)
def quick_sort(array, start, end):
    if start > end:
        return
    left = start
    right = end
    temp = array[start]

    while left != right:
        while right > left and array[right] >= temp:
            right -= 1
        while left < right and array[left] <= temp:
            left += 1
        au.exchange(array, right, left)

    array[start] = array[left]
    array[left] = temp

    quick_sort(array, start, left - 1)
    quick_sort(array, left + 1, end)


if __name__ == "__main__":
    temp_array = au.generate_array()
    print(temp_array)
    quick_sort(temp_array, 0 , len(temp_array) - 1)
    print(temp_array)

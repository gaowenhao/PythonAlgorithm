# -*- coding: utf-8 -*-
from utility import array_utility as au


# 堆排序, 整体思路就是 通过数组原有的数据结构 构建最大树结构，然后根据最大树结构调整出顺序
# 例: 49, 48, 46, 43, 40, 46, 42, 41,array[index] >= array[2*index] && array[index] >= array[2*index + 1]是一颗最大树
def max_heapify(array, depth, index):
    left_child = index << 1
    right_child = left_child + 1

    largest = index
    if left_child < depth and array[left_child] > array[largest]:
        largest = left_child
    if right_child < depth and array[right_child] > array[largest]:
        largest = right_child

    if largest != index:
        array[index], array[largest] = array[largest], array[index]
        max_heapify(array, depth, largest)


def heap_sort(array):
    for x in range(len(array) - 1, 0, -1):
        array[0], array[x] = array[x], array[0]
        max_heapify(array, x, 0)


def build_max_heap(array):
    start_index = (len(array) - 1) >> 1
    for x in range(start_index, -1, -1):
        max_heapify(array, len(array), x)


if __name__ == "__main__":
    temp_array = au.generate_array(50)
    print(temp_array)
    build_max_heap(temp_array)
    print(temp_array)
    heap_sort(temp_array)
    print(temp_array)


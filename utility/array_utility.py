# -*- coding: utf-8 -*-
import random


# 交换数组的两个元素
def exchange(array, index1, index2):
    array[index1], array[index2] = array[index2], array[index1]


# 打印数组的元素
def print_array(array):
    for var in range(30):
        print(array[var],)
    print()


# 生成一个指定大小的数组 ，如果提供参数则生成一个指定长度的数组
def generate_array(*args):
    array = []
    if len(args) < 1:
        for x in range(30):
            array.append(int(random.random() * 30))
        return array
    else:
        for x in range(args[0]):
            array.append(int(random.random() * args[0]))
        return array

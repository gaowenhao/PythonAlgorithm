# -*- coding: utf-8 -*-
import random


# 交换数组的两个元素
def exchange(array,index1,index2):
    array[index1], array[index2] = array[index2], array[index1]


# 打印数组的元素
def print_array(array):
    for var in range(30):
        print(array[var], end=",")
    print()


# 生成一个数组
def generate_array():
    array = []
    for x in range(30):
        array.append(int(random.random() * 30))
    return array


# 生成一个指定大小的数组
def generate_array(amount):
    array = []
    for x in range(amount):
        array.append(int(random.random() * amount))
    return array

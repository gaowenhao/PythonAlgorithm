# -*- coding: utf-8 -*-
from utility import array_utility as au


# 线性查找搜索 时间复杂度为O(n)
def linear_search(array, key):
    for index in range(0,len(array)):
        if array[index] == key:
            return index

if __name__ == "__main__":
    temp_array = sorted(au.generate_array(30))
    # 注意这里没有限制列表的重复，所以可能7之前就知道了，返回的并不是7
    result = linear_search(temp_array, temp_array[7])
    print(result)

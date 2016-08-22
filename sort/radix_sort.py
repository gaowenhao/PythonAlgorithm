# -*- coding: utf-8 -*-
from utility import array_utility as au
import math


# 基数排序，其方法就是选择一个基数，对个位，十位，百位...进行排序，以基数为准
# 这个算法如果基数选择10比较好理解，如果选择 4 ， 11 ，17 等数就不太容易理解
# 如果基数是4 bucket 就会有三个组，第一组用于存放 value%4余0的第二组用于存放value%4余1的，以次类推。
# 这个算法复杂度=、=，我还分析不好，这个算法一次也不需要比较，计算的次数是 n*(lg(max(n)+1),移动次数也是 n*(lg(max(n)+1)
# 这个算法需要的空间是比较大的要 O(n²)
def radix_sort(array, radix=4):
    k = int(math.ceil(math.log(max(array), radix)))  # 这里是个线性查找，搜索出现最大的值并计算他的10低的对数

    bucket = [[] for i in range(radix)]
    for i in range(1, k + 1):
        for value in array:
            bucket[value % radix ** i / radix ** (i - 1)].append(value)  # 这里先运算** 再运算 % 最后运算除法
        del array[:]
        for each in bucket:
            array.extend(each)
        bucket = [[] for i in range(radix)]


if __name__ == "__main__":
    temp_array = [42, 48, 0, 0, 48, 34, 23, 28, 34, 43]
    print(temp_array)
    radix_sort(temp_array)
    print(temp_array)

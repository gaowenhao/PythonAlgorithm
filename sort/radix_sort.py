# -*- coding: utf-8 -*-
from utility import array_utility as au
import math


def radix_sort(array, radix=10):
    k = int(math.ceil(math.log(max(array), radix)))

    bucket = [[] for i in range(radix)]
    for i in range(1, k+1):
        for value in array:
            bucket[value % radix ** i / radix ** (i-1)].append(value)
        del array[:]
        for each in bucket:
            array.extend(each)
        bucket = [[] for i in range(radix)]

if __name__ == "__main__":
    temp_array = au.generate_array()
    print(temp_array)
    radix_sort(temp_array)
    print(temp_array)

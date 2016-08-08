# -*- coding: utf-8 -*-
from utility import array_utility as au


# 希尔排序，插入排序的强化版选择一个增量，对比增量两端的数字大小小的左移，大的右移,最后执行插入排序，从而减少插入排序移动元素的个数
def shell_sort(array):
    gap = int(len(array) / 2)  # 增量(说白了就是对比数的间隔)
    while 1 <= gap:
        for outer in range(gap, len(array)):  # 增量为1以前所有的循环只是为了减少最后插入排序，移动元素的次数
            temp = array[outer]
            inner = outer - gap
            while inner >= 0 and array[inner] > temp:
                array[gap + inner] = array[inner]
                inner -= 1
            array[inner + gap] = temp
        gap = int(gap / 2)

if __name__ == "__main__":
    temp_array = au.generate_array(55)
    print(temp_array)
    shell_sort(temp_array)
    print(temp_array)

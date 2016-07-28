# -*- coding: utf-8 -*-


# 输入一个值，计算小于这个值的自然数的累加，这种是循环方式
def accumulation(key):
    temp = 0
    for x in range(key+1):
        temp += x
    print(temp)


# 递归方式实现累加
def accumulation_recursion(key):
    if key == 1:  # 设置终止条件，一直到最后才会返回1。
        return 1
    else:
        return key + accumulation_recursion(key - 1)

if __name__ == "__main__":
    print(accumulation_recursion(100))

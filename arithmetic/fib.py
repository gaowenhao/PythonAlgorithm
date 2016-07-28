# -*- coding: utf-8 -*-


# 输入一个值，返回他的斐波那契序列.
def fib(limit):
    key = 0
    temp = 1
    while key < limit:
        print key, temp,
        key = temp + key
        temp = key + temp

if __name__ == "__main__":
    fib(50)

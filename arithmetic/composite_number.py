# -*- coding: utf-8 -*-
import math


# 输入一个值，判断他是否为合数 根据定理:X为合数，则X定存在一个小于X平方根的素数为他的素数因子
# 一个合数定是N个素数因子的乘积
def is_composite_number(key):
    key_sqrt = int(math.ceil(math.sqrt(key)))
    for x in range(2, key_sqrt):
        if key % x == 0:
            return True
    return False

if __name__ == "__main__":
    print(is_composite_number(78))

# -*- coding: utf-8 -*-


# 求两个数字的最大公约数，这里用的是欧几里德算法
def gcd(key1, key2):
    mod = key1 % key2
    if mod is 0:
        return key2
    else:
        return gcd(key2, mod)


if __name__ == "__main__":
    print(gcd(11, 7))

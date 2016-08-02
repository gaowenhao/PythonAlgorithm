# -*- coding: utf-8 -*-
import array

SECURITY_KEY = 1995


# 采用简单的异或实现加密算法，根据定理：A ^ B ^ B = A
def encode(key):
    char_array = array.array('B', key)
    result = []
    for char in char_array:
        result.append(char ^ SECURITY_KEY)
    return result


def decode(security_message):
    result = []
    for char in security_message:
        result.append(chr(char ^ SECURITY_KEY))
    return "".join(result)


if __name__ == "__main__":
    temp_key = "love"
    temp_security_message = encode(temp_key)
    print(temp_security_message)
    print(decode(temp_security_message))

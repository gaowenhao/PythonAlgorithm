# -*- coding: utf-8 -*-
import string
import array

# 该算法只处理小写字母
char_array = array.array('B', string.ascii_lowercase)


# 凯撒加密算法思路很简单:就是给定明文的然后讲明文在字母表中向向后移动X个位数 abc 移动1位 就是bcd ，移动26 还是abc
# 因此可以说位移的位数就是这个加密算法的密钥
def caesar_cipher(clear_text, security_key):
    clear_array = array.array('B', clear_text)
    cipher_array = []
    for char in clear_array:
        if 97 <= char <= 122:
            cipher_array.append(chr(char_array[(char + security_key - 97) % 25]))
        else:
            cipher_array.append(chr(char))
    return ''.join(cipher_array)


def caesar_decipher(cipher_text, security_key):
    cipher_array = array.array('B', cipher_text)
    clear_array = []
    for char in cipher_array:
        if 97 <= char <= 122:
            clear_array.append(chr(char_array[25 % (abs(char - security_key - 97))]))
        else:
            clear_array.append(chr(char))
    return ''.join(clear_array)


if "__main__" == __name__:
    print(caesar_cipher('abc', 27))
    print(caesar_decipher(caesar_cipher('abc', 27), 27))

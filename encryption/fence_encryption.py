# -*- coding: utf-8 -*-


# 栅栏加密:思路把单词奇偶分割成两组，然后再拼合
# 举例 Honest 会被分割成 H n s 和 o e t 然后把这两个数组组合 oetHns就是密文了(这个算法可以应用于中文)
def fence_cipher(clear_text):
    array_odd = []
    array_even = []
    for x in range(0, len(clear_text)):
        if x % 2 == 0:
            array_even.append(clear_text[x])
        else:
            array_odd.append(clear_text[x])
    return ''.join(array_odd + array_even )


def fence_decipher(cipher_text):
    result = []
    increment = int(len(cipher_text) / 2)
    for x in range(increment, len(cipher_text)):
        result.append(cipher_text[x])
        result.append(cipher_text[x - increment] if (x - increment) < increment else '')
    return ''.join(result)


if __name__ == "__main__":
    print(fence_cipher('could you help me?'))
    print(fence_decipher(fence_cipher('could you help me?')))

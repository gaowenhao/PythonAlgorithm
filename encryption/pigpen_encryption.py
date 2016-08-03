# -*- coding: utf-8 -*-
import array
import string

# 初始化一个元组，用于保存密钥 。密钥与下面的数组对应关系为双射
cipher_key_array = (
    '0&', 'E4', '6^', '39', 'WO', '-1', '=<', '*(', '|]', 'V@', '$V', '[L', '.D', 'DR', 'N%', 'P^', ':.', 'U6', '+;',
    'O.', '*J', '#*', '/?', 'PZ', 'E(', 'I$', '  ')

# 初始化数组，用于保存基本数据(所有的特殊字符都替换成空格)
letter_array = list(string.ascii_lowercase)
letter_array.append(" ")


# 26个字母，每个字母都对应了密钥中的一个字符，加密过程就是保存字母映射到密钥中的值
def pigpen_cipher(clear_text):
    result = []
    clear_text_array = array.array('B', clear_text.lower())
    cipher_text_index = map(lambda x: abs(97 - x) if 97 <= x <= 122 else 26, clear_text_array)
    for index in cipher_text_index:
        result.append(cipher_key_array[index])
    return ''.join(result)


# 解密过程就是反向映射一次
def pigpen_decipher(cipher_text):
    result = []
    for x in range(0, len(cipher_text), 2):
        result.append(letter_array[cipher_key_array.index(cipher_text[x] + cipher_text[x + 1])])
    return ''.join(result)

if __name__ == "__main__":
    print(pigpen_cipher('could you help me ? #'))
    print(pigpen_decipher(pigpen_cipher('could you help me ? #')))

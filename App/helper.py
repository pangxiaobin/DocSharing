# -*- coding: utf-8 -*-
# @Time : 2019-10-23 20:25 
# @Author : Hubery
# @File : helper.py 
# @Software: PyCharm
"""
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
              ┏┓      ┏┓
            ┏┛┻━━━┛┻┓
            ┃      ☃      ┃
            ┃  ┳┛  ┗┳  ┃
            ┃      ┻      ┃
            ┗━┓      ┏━┛
                ┃      ┗━━━┓
                ┃  神兽保佑    ┣┓
                ┃　永无BUG！   ┏┛
                ┗┓┓┏━┳┓┏┛
                  ┃┫┫  ┃┫┫
                  ┗┻┛  ┗┻┛
"""
import uuid
from datetime import datetime
from time import time
from zlib import crc32

ALPHABET = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"


def base62_encode(num, alphabet=ALPHABET):
    """Encode a number in Base X

    `num`: The number to encode
    `alphabet`: The alphabet to use for encoding
    """
    if num == 0:
        return alphabet[0]
    arr = []
    base = len(alphabet)
    while num:
        rem = num % base
        num = num // base
        arr.append(alphabet[rem])
    arr.reverse()
    return ''.join(arr)


def base62_decode(string, alphabet=ALPHABET):
    """Decode a Base X encoded string into the number

    Arguments:
    - `string`: The encoded string
    - `alphabet`: The alphabet to use for encoding
    """
    base = len(alphabet)
    strlen = len(string)
    num = 0

    idx = 0
    for char in string:
        power = (strlen - (idx + 1))
        num += alphabet.index(char) * (base ** power)
        idx += 1

    return num


def url_to_mid(url):
    url = str(url)[::-1]
    size = len(url) // 4 if len(url) % 4 == 0 else len(url) // 4 + 1
    result = []
    for i in range(size):
        s = url[i * 4: (i + 1) * 4][::-1]
        s = str(base62_decode(str(s)))
        s_len = len(s)
        if i < size - 1 and s_len < 7:
            s = (7 - s_len) * '0' + s
        result.append(s)
    result.reverse()
    return int(''.join(result))


def mid_to_url(midint):
    midint = str(midint)[::-1]
    size = int(len(midint) / 7 if len(midint) % 7 == 0 else len(midint) / 7 + 1)
    result = []
    for i in range(size):
        s = midint[i * 7: (i + 1) * 7][::-1]
        s = base62_encode(int(s))
        s_len = len(s)
        if i < size - 1 and len(s) < 4:
            s = '0' * (4 - s_len) + s
        result.append(s)
    result.reverse()
    return ''.join(result)


def gen_mid():
    """生成唯一的mid 用于转换为url"""
    uint = str(uuid.uuid1())
    g_mid = crc32(bytes(uint, 'utf-8'))
    return g_mid


def gen_url():
    g_mid = gen_mid()
    url = mid_to_url(gen_mid())
    return url


if __name__ == '__main__':
    mid = gen_mid()
    print('mid', mid)
    uid = uuid.uuid1()
    print('uid', uid)
    url = gen_url()
    print('url', url)
    rest_mid = url_to_mid(url)
    print(rest_mid)



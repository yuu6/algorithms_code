# -*- coding:utf-8 -*-
"""
@Time:2018/5/15 21:25
@Author:yuhongchao
"""
import random
import numpy as np


def huishu(jihe):
    sum = 0
    for i in jihe:
        sum += i
    if sum % 2 != 0: print("解不存在");return
    arr = np.zeros(len(jihe))
    put_or_not(sum, jihe, arr, 0)


def put_or_not(sum, jihe, arr, index):
    if index >= len(jihe):
        print("解不存在")
        return
    # arr设置为1表示放在第一个集合，0表示放在第二个集合
    he = np.dot(jihe, arr.T)
    if he == sum / 2: print("存在解：", arr);return
    # 如果放的话
    arr[index] = 1
    if np.dot(jihe, arr.T) <= sum / 2:
        put_or_not(sum, jihe, arr, index + 1)
    # 如果不放的话
    arr[index] = 0
    put_or_not(sum, jihe, arr, index + 1)


if __name__ == "__main__":
    # li = [i for i in range(100)]
    # # 构造一个整数集合
    # jihe = random.sample(li, 20)
    jihe = [2, 3, 5, 9, 5, 4]
    jihe = np.array(jihe)
    huishu(jihe)

# -*- coding:utf-8 -*-
"""
@Time:2018/5/14 19:54
@Author:yuhongchao
"""
import sys
from sympy import Symbol,expand
import datetime

def recur(m, n):
    """
    :param m:m 是总和
    :param n:n 是最大的加数
    :return:返回的是可以划分的方式
    """
    if m < 1 or n < 1:
        return 0
    if m == 1 or n == 1:
        return 1
    if m < n:
        return recur(m, m)
    elif m == n:
        # print(str(m) + "= " + str(m - 1) + "+" + str(1))  # 输出这样一种划分的方式
        return recur(m, n - 1) + 1
    elif m > n:
        return recur(m, n - 1) + recur(m - n, n)


def dp(s, n):
    """
    :param m:总和
    :param n:最大的加数
    :return:总共可以分割的次数
    """
    arr = [([1] * (n)) for i in range(s)]
    for i in range(1, s):
        for j in range(1, n):
            arr[i][j] = arr[i - j - 1][j] + arr[i][j - 1] if j <= i else arr[i][j-1]
    return arr[n-1][s-1]

def generation_fun(s,ma):
    """
    :param s:s代表的是总数
    :param ma:最大的划分的数
    :return:可以划分的个数
    """
    x = Symbol('x')
    expr_1 = 1 #总的表达式
    for i in range(1,ma+1):#最大只能到系数是ma的情况,最小只能是1的情况
        num = int(ma/i) #如果是i的话，最多可以多少次

        expr = 1
        for j in range(1,num+1):
            expr =expr + x**(j*i)
        # print(expr)

        expr_1 *= expr
        expr_1 = expand(expr_1)

        temp_expr = 1
        for t in range(1,ma+1):
            index = expr_1.coeff(x**t)
            temp_expr += (index * x**(t))
        expr_1 = temp_expr
        # print(expr_1)

    ex = expand(expr_1)
    return ex.coeff(x**s)





if __name__ == "__main__":
    # m = 0
    # for i in range(len(sys.argv)):
    #     m = sys.argv[i]
    time1 = []
    time2 = []
    time3 = []
    for m in range(10,110,10):
        start_1 = datetime.datetime.now().timestamp()
        print("分解", m, recur(int(m), int(m)))
        end_1 = datetime.datetime.now().timestamp()
        time1.append(end_1-start_1)

        start_2 = datetime.datetime.now().timestamp()
        print("分解", m, dp(int(m), int(m)))
        end_2 = datetime.datetime.now().timestamp()
        time2.append(end_2 - start_2)

        start_3 = datetime.datetime.now().timestamp()
        print("分解", m, generation_fun(int(m), int(m)))
        end_3 = datetime.datetime.now().timestamp()
        time3.append(end_3 - start_3)

    print(time1,time2,time3)




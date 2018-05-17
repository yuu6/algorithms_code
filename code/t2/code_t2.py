# -*- coding:utf-8 -*-
"""
@Time:2018/5/15 16:59
@Author:yuhongchao
"""


def ack(m, n, arr):
    # print(m, n)
    if arr[m][n] != 0:
        return
    if m == 0:
        arr[m][n] = n + 1
        return
    if m > 0 and n == 0:
        ack(m - 1, 1, arr)
        arr[m][n] = arr[m - 1][1]
        return
    if m > 0 and n > 0:
        ack(m, n - 1, arr)
        ack(m - 1, arr[m][n - 1], arr)
        arr[m][n] = arr[m - 1][arr[m][n - 1]]
        return

def dp(m, n):
    max = 100*n
    arr = [([0] * (max)) for i in range(m + 1)]
    for i in range(m + 1):
        for j in range(max):
            if i == 0:
                arr[i][j] = j + 1
            elif j == 0:
                arr[i][j] = arr[i - 1][1]
            else:
                a = arr[i][j - 1]
                if a < max:
                    arr[i][j] = arr[i - 1][a]
                if i == m and j == n:
                    if arr[i][j] != 0:
                        return arr[i][j]
                    else:
                        break


if __name__ == "__main__":
    m = 3
    n = 5
    arr = [([0] * (100001)) for i in range(m + 1)]
    ack(m, n, arr)
    print(arr[m][n])
    print(dp(m, n))

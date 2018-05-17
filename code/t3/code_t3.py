# -*- coding:utf-8 -*-
"""
@Time:2018/5/15 20:09
@Author:yuhongchao
"""
import turtle
import random
import numpy as np
from math import *


class Dot:
    def __repr__(self):
        return "Dot(" + repr(self.xcoord) + ", " + repr(self.ycoord) + ", " + repr(self.color) + ")"

    def __init__(self, xcoord, ycoord, color):
        self.xcoord = xcoord
        self.ycoord = ycoord
        self.color = color

    def draw(self, turtle):
        turtle.goto(self.xcoord, self.ycoord)
        turtle.dot(5, self.color)


def main():
    turtle.setup(width=0.5, height=0.5, startx=0, starty=0)
    # turtle.setpos(60, 30)
    turtle.setworldcoordinates(50, 50, 500, 500)
    turtle.penup()
    turtle.speed(10)
    points = []
    for i in range(100, 500, 50):
        for j in range(100, 500, 50):
            points.append([i, j])

    for i in range(len(points)):
        dot = Dot(points[i][0], points[i][1], 'red')
        dot.draw(turtle)

    slice = random.sample(points, 10)
    slice.sort(key=lambda s: (s[0], s[1]))  # 对x进行从小到大的排序,x相同的情况下用y排序
    print(slice)
    for i in slice:
        turtle.penup()
        turtle.setposition(i[0], i[1])
        turtle.dot(8, "blue")

    tu = graham(slice)

    # turtle.penup()
    turtle.setposition(tu[0][0], tu[0][1])
    turtle.pendown()
    for i in range(1, len(tu)):
        turtle.goto(tu[i][0], tu[i][1])
    turtle.goto(tu[0][0], tu[0][1])

    turtle.getscreen()._root.mainloop()

    # 计算图形


def graham(li):
    begin = li[0]
    biaozhun = [li[0][0], -1]
    jiaodus = {}
    points = []
    points.append(li[0])
    for i in range(1, len(li)):
        cha = [begin[0] - li[i][0], begin[1] - li[i][1]]
        jiaodu = acos((cha[1] - biaozhun[1]) / sqrt(pow(cha[1] - biaozhun[1], 2) + pow(cha[0] - biaozhun[0], 2)))
        jiaodus[i] = jiaodu

    jiaos = sorted(jiaodus.items(), key=lambda item: item[1])
    print(jiaos)
    shunxus = [i[0] for i in jiaos]
    shunxus.insert(0, 0)

    # points.append(li[shunxus[1]])
    return scan(shunxus, li, points)


def scan(shunxu, li, points):
    print(shunxu)
    for i in range(len(shunxu) - 1):
        if fenge(li[shunxu[i + 1]], points[-1], li):
            points.append(li[shunxu[i + 1]])
    print(li)
    print(points)
    return points


def fenge(af, be, all):
    size = calTri(be, af, all[0])
    for i in range(1, len(all)):
        if calTri(be, af, all[i]) != size:
            return False
    return True


def calTri(p1, p2, p3):
    size = p1[0] * p2[1] + p2[0] * p3[1] + p3[0] * p1[1] - p3[0] * p2[1] - p2[0] * p1[1] - p1[0] * p3[1]
    return True if size >= 0 else False


if __name__ == '__main__':
    main()

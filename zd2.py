#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math
def circle(r):
    return math.pi * r ** 2
def cylinder():
    r = float(input("Радиус "))
    h = float(input("Высота "))
    s = 2 * math.pi * r * h
    ans = int(input("Хотите получить площадь боковой поверхности(1) или полную площадь(2) - "))
    if (ans == 1):
        print(s)
    elif(ans == 2):
        print(s + circle(r) * 2)
if __name__ == '__main__':
    cylinder()

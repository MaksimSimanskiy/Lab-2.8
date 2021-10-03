#!/usr/bin/env python3
# -*- coding: utf-8 -*-
def get_input():
    str = input("Введите строку")
    return str
def test_input(str):
    try:
        int(str)
        return True
    except ValueError:
        return False
def str_to_int(str):
    a = int(str)
    return a
def print_int(str):
    print(str)
if __name__ == '__main__':
    str = get_input()
    ans = test_input(str)
    if(ans is True):
        print_int(str_to_int(str))
    else:
        print("Не число")

# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 14:19:46 2024

@author: Student
"""

#bài 53:
def tong_1(n):
    tong=0
    for i in range(1, n+1):
        tong += i
    return tong
print(tong_1(2))

#1^2+2^2+3^2+...+n^2
def tong_2(n):
    tong=0
    for i in range(1, n+1):
        tong += i**2
    return tong
print(tong_2(3))

def tong_3(n):
    tong=0
    for i in range(1, n+1):
        tong += 1/i
    return tong
print(tong_3(2))

def tong_4(n):
    tong = 0
    giaythua =1
    for i in range(1, n+1):
        giaythua *= i
        tong += giaythua
    return giaythua
print(tong_4(2))

def tong_5(n):
    giaythua =1
    for i in range(1, n+1):
        giaythua *= i
    return giaythua
print(tong_5(3))










    
    
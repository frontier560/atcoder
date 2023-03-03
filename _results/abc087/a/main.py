#!/usr/bin/env python3

x = int(input())
a = int(input())
b = int(input())


x = x - a

while x >= b:
    x -= b

print(x)

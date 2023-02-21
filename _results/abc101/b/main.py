#!/usr/bin/env python3

num = input()
s = 0

for digit in str(num):
    s += int(digit)

if int(num)% s == 0:
    print("Yes")
else:
    print("No")

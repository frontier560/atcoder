#!/usr/bin/env python3

num = int(input())
s = input()

first = 0
second = 0
is_first=True
target = 0
index = 0
for c in s:
    if c == "|" :
        if is_first:
            is_first = False   
            first = index
        else:
            second = index
    if c == "*":
        target = index
    index += 1


if target in list(range(first,second)):
    print("in")
else:
    print("out")

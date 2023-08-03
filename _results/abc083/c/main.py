#!/usr/bin/env python3
x,y = map(int,input().split())

value = x

ans = []
i = 2
while value <= y:
    ans.append(value)
    value = value*i

print(len(ans))

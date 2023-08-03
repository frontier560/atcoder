#!/usr/bin/env python3

n,x = map(int,input().split())
a = list(map(int,input().split()))

a = list(set(a))
b = [value + x for value in a ]

c = a + b

if len(c) == len(set(c)):
    ans = "No"
else:
    ans = "Yes"

print(ans)

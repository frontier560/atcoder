#!/usr/bin/env python3
import collections

n = int(input())
blue=[]
for i in range (n):
    blue.append(input())

m = int(input())
red=[]
for i  in range (m):
    red.append(input())


blue_counter = collections.Counter(blue)
red_counter = collections.Counter(red)

ans = 0

for k,v in blue_counter.items():
    if k in red_counter:
        v = v - red_counter[k]

    ans = max(ans,v)

print(ans)

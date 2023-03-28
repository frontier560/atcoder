#!/usr/bin/env python3

n = int(input())

colors = list(map(int,input().split())) 

import collections

colors_counter = collections.Counter(colors)

ans = 0

for k,v in colors_counter.items():
    ans += v//2

print(ans)

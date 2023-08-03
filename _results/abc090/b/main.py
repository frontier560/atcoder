#!/usr/bin/env python3

a,b = map(int,input().split())

ans = 0
for n in range(a,b+1):
    if str(n) == str(n)[::-1]:
        ans += 1

print(ans)

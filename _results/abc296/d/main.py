#!/usr/bin/env python3

n,m = map(int,input().split())

ans = -2
if n * n < m:
    ans = -1
else:
    num = n
    while num * num > m:
        num -= 1

    for i in range(n+1):
        if i * num >= m:
            ans = i*num
            break

print(ans)


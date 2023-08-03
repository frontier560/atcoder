#!/usr/bin/env python3

n,k = map(int,input().split())

ans = 0
for i in range(1,n+1):
    for j in range(1,n+1):
        q,mod = divmod(i,j)
        if mod >= k:
            ans += 1

print(ans)

#!/usr/bin/env python3

n = int(input())
n_1 = list(map(int,input().split()))
n_2 = list(map(int,input().split()))

ans = 0

for i in range(1,n+1):
    value_i = sum(n_1[:i]) + sum(n_2[i-1:])
    ans = max(ans,value_i)


print(ans)

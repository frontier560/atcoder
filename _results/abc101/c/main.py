#!/usr/bin/env python3

n,k = map(int,input().split())

num_list = list(map(int,input().split()))

n = n-k

ans,mod = divmod(n,k-1)

if mod:
    ans += 1 

ans+=1
print(ans)

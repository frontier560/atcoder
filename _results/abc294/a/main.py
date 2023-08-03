#!/usr/bin/env python3

num = int(input())

a_list = list(map(int,input().split()))
ans = []
for a in a_list:
    if a % 2 == 0:
        ans.append(a)

ans = list(map(str,ans))
print(" ".join(ans))

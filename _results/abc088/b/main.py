#!/usr/bin/env python3

n = int(input())
num_list = list(map(int,input().split()))

num_list = sorted(num_list,reverse=True)

i = 0
ans= 0
for num in num_list:
    if i % 2 == 0:
        ans += num
    else:
        ans -= num
    i+=1

print(ans)

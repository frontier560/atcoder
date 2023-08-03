#!/usr/bin/env python3

a,b,k = map(int,input().split())

temp = list(range(a,b+1))

ans_list = temp[:k] + temp[k*(-1):]

ans_list = sorted(list(set(ans_list)))
for ans in ans_list:
    print(ans)

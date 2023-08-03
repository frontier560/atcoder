#!/usr/bin/env python3
n,a,b= map(int,input().split())

ans = []

def digit_sum(num:int)->int:
    num_list = []
    for digit in str(num):
        num_list.append(int(digit))

    return sum(num_list)

for i in range(1,n+1):
    if digit_sum(i) >= a and digit_sum(i) <= b:
        ans.append(i)

print(sum(ans))

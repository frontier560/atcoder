#!/usr/bin/env python3

n = int(input())

s_list = []

for i in range(n):
    s_list.append(input())

ans = "No"

for i in range(n):
    
    first = s_list[i]
    for j in range(n):

        if i == j:
            continue
        second = s_list[j]
        target = first + second
        if target == "".join(list(reversed(target))):
            ans = "Yes"
            break


print(ans)

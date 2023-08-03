#!/usr/bin/env python3

n = int(input())

a_list = list(map(int,input().split()))

ans = []
day = 0
for i in range(n):
    week = 0
    for j in range(7):
        week += a_list[day]
        day += 1
    ans.append(week)


print(*ans)

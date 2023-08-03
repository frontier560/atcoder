#!/usr/bin/env python3

n = int(input())
a_list = list(map(int,input().split()))

a_list = [0] + a_list + [0]

total = 0
for i in range(n+1):
    total += abs(a_list[i]-a_list[i+1])

for i in range(1,n+1):

    if a_list[i-1] < a_list[i+1]:


        if a_list[i-1] <= a_list[i] <= a_list[i+1]:

            print(total)
        else:
            dist = min(abs(a_list[i] - a_list[i-1]),abs(a_list[i+1] - a_list[i]))*2
            print(total - dist)
    else:
        if a_list[i-1] >= a_list[i] >= a_list[i+1]:

            print(total)
        else:
            dist = min(abs(a_list[i] - a_list[i-1]),abs(a_list[i+1] - a_list[i]))*2
            print(total - dist)


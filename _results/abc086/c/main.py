#!/usr/bin/env python3
n = int(input())

temp_x=temp_y=temp_t=count=0
for i in range(n):
    t,x ,y= map(int,input().split())
    distance =  abs(x-temp_x) + abs(y-temp_y)
    time = t-temp_t
    if time < distance:
        print("No")
        break
    elif (time- distance) % 2 == 1:
        print("No")
        break

    temp_t = t
    temp_x = x
    temp_y = y
    count += 1
if count  == n:
    print("Yes")

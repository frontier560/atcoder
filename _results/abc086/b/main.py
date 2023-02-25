#!/usr/bin/env python3

a,b = map(str,input().split())

num = int(a+b)

i = 0
while i*i <= num:

    i += 1
    if i*i == num:
        print("Yes")
        break 

if i*i != num:
    
    print("No")

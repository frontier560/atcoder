#!/usr/bin/env python3

num = int(input())

for i in range(1,num+1):

    q,mod = divmod(i,9)
    if mod == 0:
        print("9"*q)
    else:    
        print(f"{mod}"+"9"*q)

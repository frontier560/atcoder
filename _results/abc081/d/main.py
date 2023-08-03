#!/usr/bin/env python3

n = int(input())

num_list = list(map(int,input().split()))


if min(num_list) < 0:
    print(2*n)

    
else:
    print(n-1)
    for i in range(n-1):
        print(f"{i} {i+1}")



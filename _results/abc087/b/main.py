#!/usr/bin/env python3

a = int(input())
b = int(input())
c = int(input())
x = int(input())

ans = 0


for aa in range(a+1):
    for bb in range(b+1):
        for cc in range(c+1):

            if x == aa*500 + bb*100 + cc*50:
                ans +=1

print(ans)

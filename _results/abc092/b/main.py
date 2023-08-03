#!/usr/bin/env python3

n = int(input())
d,x = map(int,input().split())

ans = 0
ans += x
ans += n
choco_days = []
for i in range(n):
    
    choco = (d-1) // int(input()) 
    ans += choco



print(ans)

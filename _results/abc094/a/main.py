#!/usr/bin/env python3

a,b,x =map(int,input().split())

if a > x:
    print("NO")
elif a+b >= x:
    print("YES")
else:
    print("NO")


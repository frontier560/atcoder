#!/usr/bin/env python3

n,a,b,c,d = map(int,input().split())




if b==0 and c==0 and min([a,d])==0:
    print("Yes")

elif abs(b - c) == 1:
    print("Yes")
    

elif abs(b-c) == 0 and b>0:
    print("Yes")

else:
    print("No")


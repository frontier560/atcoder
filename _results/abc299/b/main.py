#!/usr/bin/env python3

n,t= map(int,input().split())
colors = list(map(int,input().split()))
values = list(map(int,input().split()))



if t not in colors:
    t = colors[0]


samary = zip(colors,values,list(range(1,n+1)))


qualifyed = [qualify for qualify in samary if qualify[0] == t]

winner = max(qualifyed,key= lambda x:x[1])

print(winner[2])

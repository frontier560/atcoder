#!/usr/bin/env python3
from operator import itemgetter
n = int(input())


red_points = []
blue_points = []

for i in range(n):
    a,b = map(int,input().split())
    
    red_points.append((a,b))

for i in range(n):
    a,b = map(int,input().split())
    
    blue_points.append((a,b))
blue_points.sort(key=itemgetter(0))
red_points.sort(key=itemgetter(1))

print(red_points)

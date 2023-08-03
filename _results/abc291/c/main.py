#!/usr/bin/env python3

num = int(input())

s = input()

tx = 0
ty = 0

t_list = [(0,0)]
for ss in s:

    if ss == "R":
        tx +=1
    elif ss == "L":
        tx -=1
    elif ss == "U":
        ty +=1
    elif ss == "D":
        ty -=1
    
    t = (tx,ty)
    t_list.append(t)


if len(t_list) == len(set(t_list)):
    print("No")
else:
    print("Yes")

#!/usr/bin/env python3

r,c = map(int,input().split())

field = []
is_brasted = []
for i in range(r):
    field.append(list(input()))
    is_brasted.append([False]*c)
import re
for i in range(r):
    for j in range(c):
        if re.fullmatch("\d",field[i][j]) is not None:
            bomb = int(field[i][j])

            for bi in range(r):
                for bj in range(c):
                    if abs(i - bi) + abs(j - bj) <= bomb:
                        is_brasted[bi][bj]= True
for i in range(r):
    for j in range(c):
        if is_brasted[i][j]:
            field[i][j] = "."


for i in range(r):
    print("".join(field[i]))


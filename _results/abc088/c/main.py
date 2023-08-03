#!/usr/bin/env python3

c1 = list(map(int,input().split()))
c2 = list(map(int,input().split()))
c3 = list(map(int,input().split()))

c = [c1,c2,c3]

ans = True

for i in range(3):
    if c[i][1] == c[i][2] and c[i][0] == c[i][1]:
        pass
    else:
        ans = False
    if c[1][i] == c[2][i] and c[0][i] == c[1][i]:
        pass
    else:
        ans = False


if ans:
    print("Yes")
else:
    print("No")


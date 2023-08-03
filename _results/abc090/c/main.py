#!/usr/bin/env python3

n,m = map(int,input().split())


ans = 0

if n == 1 and m == 1:
    ans = 1

elif min(n,m) == 1:
    ans = max(m,n) - 2

else:
    ans = (n - 2) * (m - 2)


print(ans)

#!/usr/bin/env python3

n = int(input())
s = input()

ans = "Yes"
for i in range(n-1):

    if s[i] == s[i+1]:
        ans = "No"
print(ans)

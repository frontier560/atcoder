#!/usr/bin/env python3

s = input()

ans = ""
temp= ""
for ss in s:
    temp += ss

    if len(temp) == 2:
        ans += temp[::-1]
        temp = ""

print(ans)

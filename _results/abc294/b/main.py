#!/usr/bin/env python3

h,w = map(int,input().split())


for i in range(h):
    num_list = list(map(int,input().split()))
    ans = ""
    for num in num_list:
        if num == 0:
            ans += "."
        else:
            ans += chr(num + 64)

    print(ans)

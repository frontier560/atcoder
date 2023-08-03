#!/usr/bin/env python3

a,b,c = map(int,input().split())

nums = sorted([a,b,c])
diff = nums[2]*2 - nums[1] -nums[0]

if diff % 2 == 0:
    print(diff//2)
else :
    print(diff//2 + 2)


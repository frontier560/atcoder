#!/usr/bin/env python3
 
s = list(input())
 
import collections
 
ans = 0
for i in range(len(s)):
    for j in range(i+1,len(s),2):
        set_count = collections.Counter(s[i:j+1])
        is_pair = True
        for v in set_count.values():
            if v % 2 == 1:
                is_pair = False
                break
        if is_pair:
            ans +=1
print(ans)


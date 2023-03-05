#!/usr/bin/env python3
import collections

n,k = map(int,input().split())

num_list = list(map(int,input().split()))


counter = collections.Counter(num_list).most_common()[::-1]
_,counts = zip(*counter)

step = len(counter)-k
ans = 0
i=0
while step > 0:
    step -= 1
    ans += counts[i]
    i += 1
    

print(ans)

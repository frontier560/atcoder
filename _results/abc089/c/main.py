#!/usr/bin/env python3

num = int(input())

s = []
for n in range(num):
    name=input()
    s.append(name[0])

march_count = []
march_count.append(s.count("M"))
march_count.append(s.count("A"))
march_count.append(s.count("R"))
march_count.append(s.count("C"))
march_count.append(s.count("H"))


ans = 0
import itertools
for v in itertools.combinations(march_count,3):

    v_count = v[0]*v[1]*v[2]
    ans += v_count

print(ans)

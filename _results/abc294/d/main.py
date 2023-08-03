#!/usr/bin/env python3
import collections

n,q = map(int,input().split())

 
#called = collections.OrderedDict()
called = {}
num = 1
for i in range(q):
    event = list(map(int,input().split()))
    if len(event)== 2:
        called.pop(str(event[1]))
    elif event[0] == 1:
        called[str(num)] = i
        num += 1
    else:
        print(next(iter(called)))

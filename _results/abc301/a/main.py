#!/usr/bin/env python3

num = int(input())

results = input()

t = 0
a = 0
for result in results:
    
    if result == "T":
        t += 1
    else :
        a += 1
    last = result

if t == a:
    if last == "T":
        print("A")
    else:
        print("T")
elif t > a:
    print("T")
else :
    print("A")

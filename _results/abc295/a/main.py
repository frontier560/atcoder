#!/usr/bin/env python3

n = int(input())

words = input().split() 

ans = "No"

if "and" in words:
    ans = "Yes"
elif "not" in words:
    ans = "Yes"
elif "that" in words:
    ans = "Yes"
elif "the" in words:
    ans = "Yes"
elif "you" in words:
    ans = "Yes"

print(ans)

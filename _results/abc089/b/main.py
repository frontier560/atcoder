#!/usr/bin/env python3

n = int(input())

hina_arare = list(input().split())

if len(set(hina_arare)) == 4:
    print("Four")
else:
    print("Three")


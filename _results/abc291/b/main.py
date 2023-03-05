#!/usr/bin/env python3

n = int(input())

score_list = list(map(int,input().split()))

score_list.sort()


del score_list[:n]
del score_list[-n:]

score = sum(score_list)/len(score_list)


                  

print(score)

#!/usr/bin/env python3

n = int(input())

a_list = list(map(int,input().split()))


uncalled= [True]*n
for i in range(n):
    
    if uncalled[i]:
        uncalled[a_list[i]-1] = False

ans = []
for i in range(n):

    if uncalled[i]:
        ans.append(i+1)
    

print(len(ans))

print(" ".join(map(str,ans)))


#!/usr/bin/env python3

n = int(input())

num_list = list(map(int,input().split()))

ans = -1
is_odd_value = True

while is_odd_value:
    ans +=1
    for i in range(len(num_list)):
        
        q,mod = divmod(num_list[i],2)
        
        if  mod == 1:
            is_odd_value=False
            break
        num_list[i] = q

print(ans)

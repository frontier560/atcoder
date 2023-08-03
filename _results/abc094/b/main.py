#!/usr/bin/env python3

n,m,x =map(int,input().split())

a_list = list(map(int,input().split()))

all_route = list(range(n))

start = all_route[0:x]
end = all_route[x:n]

start_cost = len(start + a_list) - len(set(start + a_list))
end_cost = len(end + a_list) - len(set(end + a_list))

print(min(start_cost,end_cost))

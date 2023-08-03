#!/usr/bin/env python3

n,m = map(int,input().split())

a_list = list(map(int,input().split()))
b_list = list(map(int,input().split()))


a_ans=[]
b_ans=[]
for i in range(1,len(a_list)+len(b_list)+1):

    if a_list[0] < b_list[0]:
        a_ans.append(str(i))
        del a_list[0]
        if len(a_list) == 0:
            a_list.append(9999999999)
    else:
        b_ans.append(str(i))
        del b_list[0]
        if len(b_list) == 0:
            b_list.append(9999999999)

print(" ".join(a_ans))
print(" ".join(b_ans))

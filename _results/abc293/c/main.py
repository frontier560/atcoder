#!/usr/bin/env python3

h,w = map(int,input().split())

a = []
for jj in range(w):
    a.append(list(map(int,input().split())))
ans = 0
pass_len = h + w - 1
temp =[]
i = 0
j = 0

def helper(a,pass_len,root_list):
    


    root_list.append(a[i][j])

for n in pass_len :
    
    for byte in range(2):
        if byte == 0:
            i += 1
        else:
            j +=1
        temp.append(a[i][j])


    temp.append()
    temp += ss
    for j in w:
    if len(temp) == 2:
        ans += temp[::-1]
        temp = ""


print(ans)

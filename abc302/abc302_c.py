# 題意を見る
# 全探索っぽい->DFS

import itertools

def string_diff(s,t):
    diff=0
    for i in range(len(s)):
        if s[i]!=t[i]:
            diff+=1

        if diff>1:
            break
        
    return diff

N,M=map(int,input().split())
S=[]
for i in range(N):
    S.append(input())


perm_list=itertools.permutations(S)


def f():
    for T in perm_list:
        flag=True
        for i in range(N-1):
            if string_diff(T[i],T[i+1])!=1:
                flag=False
                break
            
        if flag:
            
            return True
            
    
    return False


if f():
    print("Yes")
else:
    print("No")


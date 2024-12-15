# 整数型の入力
N,c1,c2=input().split()
N=int(N)
S=input()
T=""
for i in range(N):
    if S[i]!=c1:
        T+=c2
    else:
        T+=c1

print(T)
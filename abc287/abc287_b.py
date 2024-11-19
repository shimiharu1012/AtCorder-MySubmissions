N,M=map(int,input().split())
S=[]
T=[]
for i in range(N):
    S.append(input()[-3:])

for j in range(M):
    T.append(input())


count=0
for i in range(N):
    if S[i] in T:
        count+=1

print(count)
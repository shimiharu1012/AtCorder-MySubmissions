N=int(input())
M=0
S=[]

for i in range(N):
    s=input()
    M=len(s) if len(s)>M else M
    S.append(s)

for i in range(N):
    if len(S[i])<M:
        S[i]+="*"*(M-len(S[i]))

T=["" for _ in range(M)]
for i in range(N-1,-1,-1):
    for j in range(M):
        T[j]+=S[i][j]

for t in T:
    for k in range(len(t)-1,-1,-1):
        if t[k]!="*":
            break
    print(t[:k+1])
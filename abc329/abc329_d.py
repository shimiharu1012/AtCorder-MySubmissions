# N,M<200000 なので、素朴実装O(NM)ではTLE
# 当選者が変わるタイミングを検知したい

# トップになる可能性があるのは、さっきまでの1位 or 今票をもらった人


N,M=map(int,input().split())
A=[int(a) for a in input().split()]

votes=[0]*(N+1)
for i in range(M):
    if i==0:
        top=A[i]

    votes[A[i]]+=1

    if votes[top]<votes[A[i]]:
        top=A[i]
    if votes[top]==votes[A[i]]:
        if top>A[i]:
            top=A[i]
        


    print(top)


# ペアなので、全ての組み合わせを試せば良い

N,M=map(int,input().split())
S=[]
for i in range(N):
    S.append(input())

ans=0
for x in range(N-1):
    for y in range(x+1,N):
        Sx=S[x]
        Sy=S[y]
        for q in range(M):
            if Sx[q]=='x' and Sy[q]=='x':
                break
            
            if q==M-1:
                ans+=1

print(ans)
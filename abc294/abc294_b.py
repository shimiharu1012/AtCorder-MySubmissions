H,W=map(int,input().split())
A=[]
S=[]
for i in range(H):
    A_i=[int(a) for a in input().split()]
    S_i=""
    for j in range(W):
        if A_i[j]==0:
            S_i+='.'
        else:
            S_i+=chr(A_i[j]+ord('A')-1)

    S.append(S_i)

print(*S,sep='\n')
N,T=map(int,input().split())
C=[int(c) for c in input().split()]
R=[-1]+[int(r) for r in input().split()]


def winner():
    candidate=[]
    
    if T in C:
        color=T
    else:
        color=C[0]

    # colorが勝色

    for i in range(N):
        if color==C[i]:
            candidate.append(i)
        
    
    winner=0
    for p in candidate:
        if R[p+1]>R[winner]:
            winner=p+1

    return winner

print(winner())
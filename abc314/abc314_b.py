# Xにかけた人の番号を、かけた目の個数順で昇順に並べる
# 2次元配列を使用する


N=int(input())
A=[]
C=[]
for i in range(N):
    C.append(int(input()))
    A.append([int(a) for a in input().split()])

X=int(input())

players=[]
C_min=37
for i in range(N):
    if (X in A[i]):
        if C[i]<C_min:
            C_min=C[i]
        players.append([i+1,C[i]])

ans=[item[0] for item in players if (item[1]<=C_min)]
print(len(ans))
print(*ans)
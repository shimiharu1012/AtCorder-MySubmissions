A,B=map(int,input().split())
kouho=[1,2,3]
if A==B:
    print(-1)
else:
    print(*[kouho[i] for i in range(3) if kouho[i]!=A and kouho[i]!=B])
    
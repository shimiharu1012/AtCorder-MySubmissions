N,M=map(int,input().split())

isChamp=[True for i in range(N+1)]

for i in range(M):
    A,B=map(int,input().split())
    # 前提として、最も効率よく探してもN-1回は聞く必要がある
    # 自分より強い人が見つかればfalse
    isChamp[B]=False

for i in range(1,N+1):
    if isChamp[i]==True:
        champ=i

if sum(isChamp[1:])==1:
    print(champ)
else:
    print(-1)
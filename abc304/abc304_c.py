# 一番時間がかかる場合でも、一人ずつ感染する場合で、N
# 人同士の関係は、距離がD以内で接続する無向グラフとして表される
# 得られた無向グラフを探索すれば良い
import sys

sys.setrecursionlimit(100000)

def d(a,b):
    return (a[0]-b[0])**2+(a[1]-b[1])**2


def dfs(now):
    if visited[now]:
        return
    
    visited[now]=True
    
    for to in G[now]:
        if visited[to]:
            continue
        
        zombie.append(to)
        dfs(to)

    
    return


N,D=map(int,input().split())
positions=[]
for i in range(N):
    positions.append([int(x) for x in input().split()])

G=[[] for i in range(N)]
for i in range(N-1):
    for j in range(i,N):
        # if i==j:
        #     continue
        if  d(positions[i],positions[j])<=D**2:
            G[i].append(j)
            G[j].append(i)


visited=[False]*N
zombie=[0]

for i in range(N):
    if not visited[i] and i in zombie:
        dfs(i)

for i in range(N):
    if i in zombie:
        print("Yes")
    else:
        print("No")
H,W=map(int,input().split())
G=[]
for i in range(H):
    G.append(list(input()))

visited=[[False for j in range(W)] for i in range(H)]


now=[0,0]

while True:
    # 一度訪れた点に印をつけ、もう一度訪れるならばー1を出力
    # 操作を終了する場合はその時点での点を出力
    
    if visited[now[0]][now[1]]:
        now=-1
        break
    
    visited[now[0]][now[1]]=True

    # 点がnowではない
    if G[now[0]][now[1]]=='U' and now[0]>0:
        now=[now[0]-1,now[1]]
    elif G[now[0]][now[1]]=='D' and now[0]<H-1:
        now=[now[0]+1,now[1]]
    elif G[now[0]][now[1]]=='L' and now[1]>0:
        now=[now[0],now[1]-1]
    elif G[now[0]][now[1]]=='R' and now[1]<W-1:
        now=[now[0],now[1]+1]
    else:
        break

    


if now==-1:
    print(now)
else:
    print(now[0]+1,now[1]+1)
    
    

# H*N=<25000
# N=<500
# したがって、全てのマスを調べれば良い


H,W,N=map(int,input().split())
T=input()
Board=[]

def move(pos,dir):

    if dir=='L':
        to=[pos[0],pos[1]-1]
        if to[1]<0:
            return False
        elif Board[to[0]][to[1]]=='#':
            return False

    elif dir=='R':
        to=[pos[0],pos[1]+1]
        if to[1]>W-1:
            return False
        elif Board[to[0]][to[1]]=='#':
            return False
        
    elif dir=='U':
        to=[pos[0]-1,pos[1]]
        if to[0]<0:
            return False
        elif Board[to[0]][to[1]]=='#':
            return False
        
    elif dir=='D':
        to=[pos[0]+1,pos[1]]
        if to[0]>H-1:
            return False
        elif Board[to[0]][to[1]]=='#':
            return False

    return to
    


for i in range(H):
    Board.append(input())

count=0
for i in range(H):
    for j in range(W):
        cur=[i,j]
        if Board[cur[0]][cur[1]]=='#':
            continue
        else:
            ok=True
            for dir in T:
                to=move(cur,dir)
                if to==False:
                    ok=False
                    break
                cur=to[:]
        if ok:
            # print(i,j)
            count+=1
                
print(count)




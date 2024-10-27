H,W=map(int,input().split())
Board=[]
for i in range(H):
    Board.append(list(input()))


def f():
    # 縦を調べる
    for j in range(W):
        for i in range(H-4):
            if [Board[i+k][j] for k in range(5)]==['s','n','u','k','e']:
                return [(i+k+1,j+1) for k in range(5)]
            elif [Board[i+k][j] for k in range(5)]==['s','n','u','k','e'][::-1]:
                return [(i+k+1,j+1) for k in range(5)][::-1]
                

    # 横を調べる
    for i in range(H):
        for j in range(W-4):
            if [Board[i][j+k] for k in range(5)]==['s','n','u','k','e']:
                
                return [(i+1,j+k+1) for k in range(5)]
            elif [Board[i][j+k] for k in range(5)]==['s','n','u','k','e'][::-1]:
                return [(i+1,j+k+1) for k in range(5)][::-1]
    

    # 左上から右下
    for i in range(H-4):
        for j in range(W-4):
            if [Board[i+k][j+k] for k in range(5)]==['s','n','u','k','e']:
                return [(i+k+1,j+k+1) for k in range(5)]
            elif [Board[i+k][j+k] for k in range(5)]==['s','n','u','k','e'][::-1]:
                return [(i+k+1,j+k+1) for k in range(5)][::-1]
            
    # 右上から左下
    for i in range(H-4):
        for j in range(4,W):
            if [Board[i+k][j-k] for k in range(5)]==['s','n','u','k','e']:
                return [(i+k+1,j-k+1) for k in range(5)]
            elif [Board[i+k][j-k] for k in range(5)]==['s','n','u','k','e'][::-1]:
                return [(i+k+1,j-k+1) for k in range(5)][::-1]

    
for item in f():
    print(*item)
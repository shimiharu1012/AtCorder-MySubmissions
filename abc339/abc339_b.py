H,W,N=map(int,input().split())
Board=[['.' for j in range(W)] for i in range(H)]
# tの方向と座標をもとに
# t+1の方向と座標を返す

def rotate_right(dir):
    if dir==[-1,0]:
        return [0,1]
    elif dir==[0,1]:
        return [1,0]
    elif dir==[1,0]:
        return [0,-1]
    else:
        return [-1,0]

def rotate_left(dir):
    if dir==[-1,0]:
        return [0,-1]
    elif dir==[0,-1]:
        return [1,0]
    elif dir==[1,0]:
        return [0,1]
    else:
        return [-1,0]

pos=[0,0]
dir=[-1,0]

def turn(dir,pos):
    if Board[pos[0]][pos[1]]=='.':
        Board[pos[0]][pos[1]]='#'
        dir=rotate_right(dir)
    else:
        Board[pos[0]][pos[1]]='.'
        dir=rotate_left(dir)
    
    pos=[
        (pos[0]+dir[0])%H,
        (pos[1]+dir[1])%W
    ]

    return [dir,pos]

for t in range(N):
    dir,pos=turn(dir,pos)

for row in Board:
    print(*row,sep='')
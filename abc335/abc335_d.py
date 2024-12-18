# Nは小さいので計算量は考えなくて良い

N=int(input())

# 右回りで内側に向かって巻いていく
# posの現在の向きを定義して、条件分岐すれば良い

def turn_right():
    if cur['abs_dir']=='E':
        cur['abs_dir']='S'
    elif cur['abs_dir']=='S':
        cur['abs_dir']='W'
    elif cur['abs_dir']=='W':
        cur['abs_dir']='N'
    elif cur['abs_dir']=='N':
        cur['abs_dir']='E'

def move():

    
    if cur['abs_dir']=='E':
        if cur['pos'][1]>=N-1 or Grid[cur['pos'][0]][cur['pos'][1]+1]!='.':
            turn_right()
        else:
            cur['pos'][1]+=1
            Grid[cur['pos'][0]][cur['pos'][1]]=cur['number']
            cur['number']+=1
    elif cur['abs_dir']=='W':
        if cur['pos'][1]<=0  or Grid[cur['pos'][0]][cur['pos'][1]-1]!='.':
            turn_right()
        else:
            cur['pos'][1]-=1
            Grid[cur['pos'][0]][cur['pos'][1]]=cur['number']
            cur['number']+=1
    elif cur['abs_dir']=='S':
        if cur['pos'][0]>=N-1 or Grid[cur['pos'][0]+1][cur['pos'][1]]!='.':
            turn_right()
        else:
            cur['pos'][0]+=1
            Grid[cur['pos'][0]][cur['pos'][1]]=cur['number']
            cur['number']+=1
    elif cur['abs_dir']=='N':
        if cur['pos'][0]<=0  or Grid[cur['pos'][0]-1][cur['pos'][1]]!='.':
            turn_right()
        else:
            cur['pos'][0]-=1
            Grid[cur['pos'][0]][cur['pos'][1]]=cur['number']
            cur['number']+=1
    


cur={'pos':[0,0],'abs_dir':'E','number':1}
Grid=[['.' for _ in range(N)] for _ in range(N)]
Grid[0][0]=cur['number']
cur['number']+=1
t=0
while True:
    if cur['pos']==[N//2,N//2]:
        Grid[cur['pos'][0]][cur['pos'][1]]='T'
        break
    move()
    t+=1

    
    
for i in range(N):
    print(*Grid[i])

H,W=map(int,input().split())
S1,S2=map(int,input().split())
Board=[]
for i in range(H):
    Board.append(input())
X=input()

def U(pos):
    
    return [pos[0]-1,pos[1]] if pos[0]>0 and Board[pos[0]-1][pos[1]]=='.' else pos

def D(pos):
    return [pos[0]+1,pos[1]] if pos[0]<H-1 and Board[pos[0]+1][pos[1]]=='.'else pos
    
def L(pos):
    return [pos[0],pos[1]-1] if pos[1]>0  and Board[pos[0]][pos[1]-1]=='.' else pos

def R(pos):
    return [pos[0],pos[1]+1] if pos[1]<W-1  and Board[pos[0]][pos[1]+1]=='.' else pos


cur=[S1-1,S2-1]

for x in X:
    if x=='L':
        cur=L(cur)
    elif x=='R':
        cur=R(cur)
    elif x=='U':
        cur=U(cur)
    elif x=='D':
        cur=D(cur)




print(cur[0]+1,cur[1]+1)

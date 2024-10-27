# 2x2より大きな矩形領域から、かけた部分を求める
# 計算量を考える必要はない
# a,b,c,dを求める
# 次に、a,b,c,dの範囲を調べて、出力を行う

H,W=map(int,input().split())
Board=[]
for i in range(H):
    Board.append(list(input()))

a,b,c,d=-1,-1,-1,-1
for i in range(H):
    if '#' in Board[i]:
        if a<0:
            a=i
        else:
            b=i

for j in range(W):
    if '#' in [Board[i][j] for i in range(H)]:
        if c<0:
            c=j
        else:
            d=j

def f():
    for i in range(a,b+1):
        for j in range(c,d+1):
            if Board[i][j]=='.':
                return (i+1,j+1)
            

print(*f())
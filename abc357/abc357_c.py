# 出力自体を再帰的に行うのは難しい
# したがって、カーペットの展開を再起的に行う

# recの返り値は必ず二重のリストであることに注意
def Sierpinski(K):
    Grid=[]
    if K==0:
        return [["#"]]
    else:
        # 中央が3**k-1ずつの白います
        center=[['.' for _ in range(3**(K-1))] for _ in range(3**(K-1))] 
        return make_carpet(Sierpinski(K-1),center)
        
def make_carpet(around,center):
    # 2重リストを受け取り、それを元にカーペットを作成
    Carpet=[]
    H=len(around)
    
    # Carpetの上1/3を作成する
    for i in range(H):
        row=around[i]+around[i]+around[i]
        Carpet.append(row)

    # Carpetの中央1/3を作成
    for i in range(H):
        row=around[i]+center[i]+around[i]
        Carpet.append(row)

    # Carpetの下1/3を作成する
    for i in range(H):
        row=around[i]+around[i]+around[i]
        Carpet.append(row)

    return Carpet

    


N=int(input())
ans=Sierpinski(N)

for row in ans:
    print(''.join(row))
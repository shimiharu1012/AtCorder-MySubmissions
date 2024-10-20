# 広いグリッドが与えられるので、1つずつずらして調べて条件を満たすか調べる

def Is_TakCode(matrix):
    # 左上の3x3が黒かどうか調べる
    # 左上の3x3の周囲7マスが白かどうかを調べる
    for i in range(3):
        if matrix[i][:4]!='###.':
            return False
    if matrix[3][:4]!="....":
        return False

    # 右下の3x3が黒かどうか調べる
    # 右下の3x3の周囲7マスが白かどうかを調べる
    if matrix[-4][-4:]!="....":  
        return False
        
    for i in range(6,9):
        if matrix[i][-4:]!='.###':
            return False
    


    return True


N,M=map(int,input().split())
Board=[]
for i in range(N):
    Board.append(input())

count=0
for i in range(0,N-9+1):
    for j in range(0,M-9+1):
        # 左上のますがi,jから始まる9x9の領域を持ってくる
        covered=[row[j:j+9] for row in Board[i:i+9]]
        if Is_TakCode(covered):
            print(i+1,j+1)


    

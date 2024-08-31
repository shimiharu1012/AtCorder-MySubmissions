# i枚目のシートは
# x: Ai<=x<=Bi
# y: Ci<=y<=Di　をカバーしている
# シートが重複することを踏まえて、シートで覆われる面積を求める
# 1次元で考えてから拡張

N=int(input())

area=[[0 for i in range(100)] for j in range(100)]

# 繰り返せるので、N回のクエリに対して。100*100のエリアを全て調査する
for i in range(N):
    A_B_C_D=[int(x) for x in input().split()]
    A=A_B_C_D[0]
    B=A_B_C_D[1]
    C=A_B_C_D[2]
    D=A_B_C_D[3]

    for x in range(A,B):
        for y in range(C,D):
            area[x][y]=1

S=0
for i in range(100):
    for j in range(100):
        S+=area[i][j]

print(S)
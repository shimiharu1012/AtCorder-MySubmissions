# 計算量を考える
# M<2x10^5
# 駒が置けないマスを重複しないで数える必要がある
# これをどのように実現するか

N,M=map(int,input().split())
# NG=set()
NG=[]
for i in range(M):
    a,b=map(int,input().split())
    moves = [
        (a + 2, b + 1), (a + 1, b + 2), (a - 1, b + 2), (a - 2, b + 1),
        (a - 2, b - 1), (a - 1, b - 2), (a + 1, b - 2), (a + 2, b - 1)
    ]
    NG.append((a,b))
    for i in range(8):
        if 0<moves[i][0]<N+1 and 0<moves[i][1]<N+1:
            # to.append(moves[i])
            NG.append(moves[i])

    # print(to)
    # NG=NG|set(to)|set([(a,b)])

# print(NG)
# print(len(NG))
# print(len(set(NG)))
# print(NG)
print(N**2-len(set(NG)))
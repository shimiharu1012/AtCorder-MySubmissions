# HをGと同型になるように変更する
# まず、Gと同型な任意のグラフをWとし、
# H->Wのコストが最小のものを選択すれば良い
# ここにおいて、

from itertools import permutations



N=int(input())
E_G=[]
E_H=[]

M_G=int(input())
for i in range(M_G):
    E_G.append(sorted([int(x) for x in input().split()]))

M_H=int(input())
for i in range(M_H):
    E_H.append(sorted([int(x) for x in input().split()]))

A=[]
for i in range(N-1):
    A.append([int(Aij) for Aij in input().split()])

# N!通りの変形後パターンを全て調べれば良い

W_list=[list(x) for x in permutations(range(1,N+1))]
# print(W_list)

# G同型なグラフWをN!-1通り全て調べて、変形コストが最小の0より大きい最小のものを調べる
cost_list=[]
for W in W_list:
    # (1,2,3,4...)を入れ替えたWに対して、同型性を保つ辺集合を作る
    E_W=[sorted([W[e[0]-1],W[e[1]-1]]) for e in E_G]
    # E_HをE_Wにするためのコストを計算する
    # Hから余分な辺を削除するためのコスト
    cost=0
    for e in E_H:
        if e not in E_W:
            cost+=A[e[0]-1][e[1]-e[0]-1]
    # Hに足りない辺を追加するためのコスト
    for e in E_W:
        if e not in E_H:
            cost+=A[e[0]-1][e[1]-e[0]-1]
    
    cost_list.append(cost)
print(min(cost_list))
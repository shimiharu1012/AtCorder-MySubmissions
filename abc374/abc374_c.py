# N個の部署をA,Bに割り当てる
# つまり、Kこの整数を二つのグループに分けるという条件のもとで
# １つのグループの最大人数として最小のものを求めたい
# 一番小さいのは,Nこの部署に１人ずつの時、N/2人


# Nこのものを2グループに分ける方法はたかだか2^20通り
# bit全探索でいける？

from itertools import product

N=int(input())
K=[int(k) for k in input().split()]
total=sum(K)

MIN=10**10
for bit_array in product((0,1),repeat=N):

    A=sum([bit_array[i]*K[i] for i in range(N)])
    B=total-A

    if max(A,B)<MIN:
        MIN=max(A,B)
    
print(MIN)
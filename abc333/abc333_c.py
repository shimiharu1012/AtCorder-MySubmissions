# レピュニット:1,11,111,1111...

# 範囲：３つのレピュニットの輪として表せる整数
# 条件：N番目に小さいもの

# POINT：３レピュニットの和がどういう順番になるかわからない
# ３レピュニットの和の判定が非自明
# 333番目までのレピュニット３つの和は、1,11....1*12からなる
import math

N=int(input())

n=1
while True: 
    if math.comb(n+3-1,3)>333:
        break
    n+=1

repunits=[1]
for i in range(11):
    repunits.append(repunits[-1]+10**(i+1))

sums=[]
for i in range(12):
    for j in range(i,12):
        for k in range(j,12):
            sums.append(repunits[i]+repunits[j]+repunits[k])


print(sorted(sums)[N-1])
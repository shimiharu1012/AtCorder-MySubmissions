# 整数型の入力
# N人農地、身長がx以上の生徒の人数
# N<200000なので、各クエリに対してfor文で回すとTLE
# したがって、各クエリに対して２分探索で真ん中を求める

import bisect

N,Q=map(int,input().split())
A=sorted([int(a) for a in input().split()])

for i in range(Q):
    x=int(input())
    # Amidは、身長がx未満の生徒の人数
    mid=bisect.bisect_left(A,x)
    print(N-mid)
    


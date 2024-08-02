# main2の実装を踏襲する
# 結局計算するので、判定のみのロジックは不要

N=int(input())
L=[]
R=[]
sum_L=0
# X=[]
for i in range(N):
    l,r=map(int,input().split())
    sum_L+=l
    L.append(l)
    R.append(r)

    # [L1,L2...LN]からスタートし、前の要素から順に足していって
    # sum(L1,L2...LN)=0になるまで繰り返す
    # ただし、1ずつ足していくとTLEする(sum(L)と0の差が大きいため)

# OK
if sum_L>0:
    print("No")
else:
    for i in range(N):
        add=min(0-sum_L,R[i]-L[i])
        L[i]+=add
        sum_L+=add

        if sum_L==0:
            break

        # if (0-sum_L)>(R[i]-L[i]):
        #     # L[i]->R[i]にしてもまだ条件を満たさない
        #     # ワンチャンsum(L)の再計算でTLEするかも
        #     sum_L=sum_L-L[i]+R[i]
        #     L[i]=R[i]
        # else:
        #     # L[i]を調整して、解Xが得られる
        #     L[i]+=(0-sum_L)
        #     sum_L=0

    if sum_L==0:
        print("Yes")
        print(*L)
    else:
        print("No")
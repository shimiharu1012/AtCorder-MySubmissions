import bisect

N,T=map(int,input().split())
A=[int(a) for a in input().split()]
F=[A[0]]
for i in range(1,N):
    F.append(F[-1]+A[i])
cycle=F[-1]
# 曲が終わる時間を配列Fとしてもつ
# Fiが始めてT以上になるタイミングを探す
# 2分探索
# プレイリスt１周分を法としてmodをとる必要がある

ln=T//cycle
t=T-cycle*ln
# 1<F[-1]-1
num=bisect.bisect_right(F,t)
# num番目の途中に終了する
print(num+1,A[num]-F[num]+t)

# 一番お得に回りたい
# どんな日に対して、周遊パスを購入するとお得か
# DxPよりも和が大きい場合、お得

N,D,P=map(int,input().split())
F=sorted([int(f) for f in input().split()],reverse=True)

total=0
# D日ごとに分けて、パスがお得かを検証
for b in range(N//D):
    if sum(F[D*b:D*(b+1)])>P:        
        total+=P
    else:
        total+=sum(F[D*b:D*(b+1)])
    


# 残り日数に対して、それでもパスの方がお得かを調べる
if sum(F[D*(N//D):N])>P:
    total+=P
else:
    total+=sum(F[D*(N//D):N])


print(total)
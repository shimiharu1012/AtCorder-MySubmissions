# バスの乗客は常に0以上になる
# バスの乗客が-になる場合、最小の時点での0との差を加算する

N=int(input())
A=[int(a) for a in input().split()]


p=0
MIN=0
for i in range(N):
    p+=A[i]
    if p<MIN:
        MIN=p

print(p+(-MIN))



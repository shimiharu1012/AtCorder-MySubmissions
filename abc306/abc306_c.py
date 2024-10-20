# 1,2,3...Nがちょうど３回ずつ現れる長さ3Nの数列
# 題意がややこしいので、まず素朴実装

# Aに3回登場する1のうち、真ん中のやつはどこにあるか？
# count=[0]を持っておき、Aを舐めて、2回目の登場の場合はそのインデックスを

N=int(input())
A=['.']+[int(a) for a in input().split()]
count=[0]*(N+1)
items=[(0,0)]

for i in range(1,3*N+1):
    count[A[i]]+=1
    if count[A[i]]==2:
        items.append((i,A[i]))

print(*[y[1] for y in sorted(items,key=lambda x:x[0])][1:])

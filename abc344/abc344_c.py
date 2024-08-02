N=int(input())
A=[int(a) for a in input().split()]
M=int(input())
B=[int(b) for b in input().split()]
L=int(input())
C=[int(c) for c in input().split()]
Q=int(input())
X=[int(x) for x in input().split()]

# A,B,Cから要素を1つずつ選び、X_iを作ることができるか
# X_iに対して、全ての組み合わせを試すとTLE
# A,B,Cの全てのパターンの和を先に計算して
# 後からX_iに一致するものがあるかを調べる

all_sums=set()
for a in A:
    for b in B:
        for c in C:
            all_sums.add(a+b+c)

for x in X:
    if x in all_sums:
        print("Yes")
    else:
        print("No")
        



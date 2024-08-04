# Aの中で2番目に大きい要素のインデックス
# Nは十分小さいが、Aが大きい（10^9）
# つまり、メモリが足りない？
# A1~ANは全て異なる

N=int(input())

i_A={}
A=[int(a) for a in input().split()]
for i in range(N-1,-1,-1):
    i_A[i]=A.pop()

i_A=sorted(i_A.items(),key=lambda x:x[1],reverse=True)

print(i_A[1][0]+1)


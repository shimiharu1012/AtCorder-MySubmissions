N=int(input())
A=[0]+[int(a) for a in input().split()]+[0]

# 1-Nを全て回った場合の合計金額totalをもとめて
# i=1~Nについて
# totalから,Aiを含む経路の金額を引けば良い
# ただし、i=1,Nの時（コーナーケース）は怪しい
total=0
for i in range(N+1):
    total+=abs(A[i]-A[i+1])


for i in range(1,N+1):
    sub=abs(A[i-1]-A[i])+abs(A[i]-A[i+1])
    add=abs(A[i-1]-A[i+1])
    print(total-sub+add)
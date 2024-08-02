N=int(input())
A=[int(a) for a in input().split()]
A=sorted(A,reverse=True)

A_max=A[0]

for i in range(N):
    if A[i]!=A_max:
        print(A[i])
        break



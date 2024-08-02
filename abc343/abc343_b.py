N=int(input())
A=[]
for i in range(N):
    # A.append([int(a_ij) for a_ij in input().split()])
    A_i=[int(a_ij) for a_ij in input().split()]
    print(*[j+1 for j in range(N) if A_i[j]==1])


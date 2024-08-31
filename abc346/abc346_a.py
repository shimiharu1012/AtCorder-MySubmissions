N=int(input())
A=[int(a) for a in input().split()]

B=[A[i]*A[i+1] for i in range(N-1)]
print(*B)
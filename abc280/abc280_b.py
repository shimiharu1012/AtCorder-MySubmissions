N=int(input())
S=[int(s) for s in input().split()]

A=[S[0]]
for i in range(N-1):
    A.append(S[i+1]-S[i])

print(*A)
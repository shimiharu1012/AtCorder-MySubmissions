N,H,X=map(int,input().split())
P=[int(p) for p in input().split()]

for i in range(N):
    if H+P[i]>=X:
        break

print(i+1)
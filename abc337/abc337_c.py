N=int(input())
A=[int(a) for a in input().split()]
D={A[i]:i+1 for i in range(N)}


for item in D.items():
    if item[0]==-1:
        front=item[1]

raw=[front]


for _ in range(N-1):
    front=D[front]
    raw.append(front)

print(*raw)
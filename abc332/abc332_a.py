N,S,K=map(int,input().split())
cost=0
for i in range(N):
    P,Q=map(int,input().split())
    cost+=P*Q

if cost<S:
    cost+=K

print(cost)
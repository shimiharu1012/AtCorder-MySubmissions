# 箱の個数＝荷物の個数＝N
# 各箱の一番重いものを除いて全て移動する
# そのためのコストは、箱の中の総和-最大値

total_cost=0
N=int(input())
A=[int(a) for a in input().split()]
W=[int(w) for w in input().split()]

box=[[] for _ in range(N)]
for i in range(N):
    box[A[i]-1].append(W[i])

for i in range(N):
    if len(box[i])>1:
        total_cost+=(sum(box[i])-max(box[i]))
    
print(total_cost)

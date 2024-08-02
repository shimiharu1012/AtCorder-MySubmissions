# なるべく多くの人数が会議に参加できる時間帯において
# 会議に参加できる人数


# したがって、ある社を基準とし
# 基準の社における全ての場合の時間帯を調べる


N=int(input())
W_X=[]
for i in range(N):
    W_X.append([int(x) for x in input().split()])


p_max=0
for t in range(0,25):
    diff=t-W_X[0][1]
    p=0
    for i in range(N):
        # 各社について、
        # １社目を基準とした時の各社の時間帯と
        # 会議に参加可能であれば人数を加算する
        w=(W_X[i][1]+diff)%24
        if w>=9 and w<=17:
            p+=W_X[i][0]

    if p>p_max:
        p_max=p

print(p_max)
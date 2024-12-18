N,Q=map(int,input().split())

# 龍をどのようなデータ構造でもつか
# 連結リスト(deque)は両端の追加削除が早いが、
# ランダムアクセスできないため、中央付近へのアクセスが遅い
# 特にpythonにおけるcollections.dequeの実装ではそれが影響してしまう
import collections

# [x,y]
dragon=[[i+1,0] for i in range(N)][::-1]


def move(dir):
    if dir=='R':
        pos_head=[dragon[-1][0]+1,dragon[-1][1]]
        dragon.append(pos_head)
    elif dir=='L':
        pos_head=[dragon[-1][0]-1,dragon[-1][1]]
        dragon.append(pos_head)
    elif dir=='U':
        pos_head=[dragon[-1][0],dragon[-1][1]+1]
        dragon.append(pos_head)
    elif dir=='D':
        pos_head=[dragon[-1][0],dragon[-1][1]-1]
        dragon.append(pos_head)

for _ in range(Q):
    query_type,query_input=input().split()

    if query_type=='1':
        move(query_input)
    elif query_type=='2':
        p=int(query_input)
        print(*dragon[-p])
        
# H 初めの体力 
# M 体力の回復アイテム個数 
# N回の移動
# S 移動の方向（長さNの文字列）

# 体力が負になると強制終了
# 一度も倒れることなくN回の移動を終えることができるか


def move_pos(pos,dir):
    if dir=='R':
        pos[0]+=1
    elif dir=='L':
        pos[0]-=1
    elif dir=='U':
        pos[1]+=1
    elif dir=='D':
        pos[1]-=1


N,M,H,K=map(int,input().split())
S=input()
items=set()

# アイテムがあるかどうかを辞書で管理


# アイテムがある座標をTrueにする
for i in range(M):
    x,y=map(int,input().split())
    items.add((x,y))

pos_cur=[0,0]
hp=H
Board=[]
# 処理の順番
# 体力を判定
# 移動　体力を減らす
# アイテムがあれば使って、体力をKに回復

# 移動回数
count_move=0

while True:

    # 移動し、体力を減らす
    if hp>=0:
        move_pos(pos_cur,S[count_move])
        count_move+=1
        hp-=1
    else:
        break
    # 体力が負になったら終了
    if hp<0:
        break
    
    #体力がK未満の場合
    if hp<K:
        # アイテムがあるかどうかを判定
        if (pos_cur[0],pos_cur[1]) in items:
            hp=K
            items.remove((pos_cur[0],pos_cur[1]))

    if count_move>=N:
        break

if hp<0:
    print("No")
else:
    print("Yes")
# N種類のビーンズが1粒ずつある
# i種類目(1~N)のビーンズは
# おいしさAi,色Ci
# ビーンズは混ざっているので、色でしか区別できない
# （味では区別できない）

# 食べる可能性のあるビーンズのおいしさの最小値を最大化する色の選び方
# 色ごとにビーンズを分けて、各色のグループの中のおいしさの最小値を比較し
# 最大のグループ（色）を選べば良い

N=int(input())
beans_group_by_color={}

for i in range(N):
    A,C=map(int,input().split())
    try:
        beans_group_by_color[C].append(A)
    except KeyError as e:
        beans_group_by_color[C]=[A]
        
MIN=0
best_color=-1
for key in beans_group_by_color:
    if min(beans_group_by_color[key])>MIN:
        best_color=key
        MIN=min(beans_group_by_color[best_color])

print(min(beans_group_by_color[best_color]))
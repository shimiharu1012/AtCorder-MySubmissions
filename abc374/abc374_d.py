# 選択する直線の順番はN通り
# そのうち、始点と終点の選び方は2通り
# したがって、調べるルートの数(2xN)*(2x(N-1))...通り

# 少ないループで綺麗に調べる方法を考える
# 結局、全ての組み合わせを全探索する必要がありそう
# ループ数が入力依存なので、

from itertools import permutations
from itertools import product
import math

def distance(p1,p2):
    d=math.sqrt((p1[0]-p2[0])**2+(p1[1]-p2[1])**2)
    return d

points=[]
N,S,T=map(int,input().split())
for i in range(N):
    A,B,C,D=map(int,input().split())
    points.append([A,B])
    points.append([C,D])


times=[]
# nowは現在の位置 timeはそれまでに経過した時間
def dfs(now,time,visited):
    
    # 未訪問の点がこの時点でなければ終了
    if sum(visited)==len(points):
        times.append(time)
        return


    # 未訪問の点を全て始点に設定し、さらに続きを掘る
    for start in range(len(points)):
        if visited[start]:
            continue
        
        temp_time=time
        #　nowからstartまで移動し、時間を経過
        temp_time+=distance(now,points[start])/S

        if start%2==0:
            end=start+1
            temp_time+=distance(points[start],points[end])/T
        else:
            end=start-1
            temp_time+=distance(points[start],points[end])/T

        visited[start]=True
        visited[end]=True
        dfs(points[end],temp_time,visited)

        # バックトラッキング
        visited[start]=False
        visited[end]=False   
    


dfs([0.,0.],0,[False]*len(points))


print(min(times))

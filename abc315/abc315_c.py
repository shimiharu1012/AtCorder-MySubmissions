# 順番はどうでも良い
# NlogNには納めたい
# N個から2つ選ぶ。ただし選び方が特殊
# 味をキーにして保存してまとめておく
# それとは別に、おいしさが上位のものを保存しておく
# 実際に覚えておくべき情報
# 最も美味しい二つのアイス
# 味が異なる最も美味しい２つのアイス
# したがって、たかだか３つのアイスを覚えておけば良い
# 3つのアイスを覚えておき、上２つが異なる味なら、その和が最大
# 上２つが同じなら、1+3と、1+2/2を比較する
# １番目-k番目が同じ味の場合もある
# したがって、１番目の味と異なる味のうち、最も美味しいものを探す必要がある


N=int(input())

top_2=[[0,0],[0,0]]
F=[]
S=[]
for i in range(N):
    f,s=map(int,input().split())
    
    if s>top_2[-1][1]:

        top_2=[top_2[0]]+[[f,s]]

        top_2=sorted(top_2,key=lambda x:x[1],reverse=True)

    F.append(f)
    S.append(s)

dif_F_max=max([S[i] for i in range(N)  if F[i]!=top_2[0][0]]+[-1])

if top_2[0][0]!=top_2[1][0]:
    print(top_2[0][1]+top_2[1][1])
else:
    print(max(top_2[0][1]+top_2[1][1]//2,top_2[0][1]+dif_F_max))

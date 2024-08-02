N=int(input())
cards={}

for i in range(N):
    A,C=map(int,input().split())
    cards[i+1]=(A,C)

# カードの強さ順んで並べ替える
cards=sorted(cards.items(),key=lambda item:item[1][0],reverse=True)

# 全てのカードに対して、

# Ax=Ayの時、Cx>Cyでも良い
# Ax<Ayの時、Cx>Cyなら、xを捨てる

while True:
    # 一番最初のカードは、必ず入る
    new_cards=[cards[0]]
    # 2枚目のカードから調べる
    for x in range(len(cards)-1):
        y=x+1
        if  cards[x][1][0]==cards[y][1][0]:
            # 強さが一緒の時、コストに関わらず残す
            new_cards.append(cards[y])
        elif    cards[x][1][1]> cards[y][1][1]:
            # 強さがx>yの場合、コストがx>=yであればカードyを残す
            new_cards.append(cards[y])

    if len(new_cards)==len(cards):
        break
    else:
        cards=new_cards[:]

print(len(new_cards))
print(*[x[0] for x in sorted(new_cards)],sep=' ')
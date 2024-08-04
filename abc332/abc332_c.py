N,M=map(int,input().split())
S=input()

# 無地がMまい
# ロゴ入りを何枚購入すべきか
no_logo=M
# i番目の要素は、i日目でのlogoTの不足分
logo_shortages=[0]
for i in range(N):
    if S[i]=='0':
        no_logo=M
        logo_shortages.append(0)
    elif S[i]=='1':
        if no_logo>0:
            no_logo-=1
            logo_shortages.append(logo_shortages[-1])
        else:
            logo_shortages.append(logo_shortages[-1]-1)
    elif S[i]=='2':
        logo_shortages.append(logo_shortages[-1]-1)


print(-min(logo_shortages))

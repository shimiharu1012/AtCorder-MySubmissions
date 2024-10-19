# 26文字であることを生かす
# 累積和で、すべてのアルファベットの出現回数をあらかじめ調べる
# 範囲内に含まれるアルファベットの個数を調べる

S=input()
N=len(S)


ans=0

for c in list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'):

    acm=[0]
    for i in range(N):
        if S[i]==c:
            acm.append(acm[-1]+1)
        else:
            acm.append(acm[-1])

    for j in range(2,N):
        # 文字列Sについて、0文字目からN文字目までの、cの累積の出現回数を調べる
            
            # jよりも前でcが出現する場所の数を累積和を元に求める
            i_num=(acm[j-1])
            
            # jよりも後でcが出現する場所の数を累積和を元に求める
            k_num=(acm[N]-acm[j])

            ans+=i_num*k_num

print(ans)
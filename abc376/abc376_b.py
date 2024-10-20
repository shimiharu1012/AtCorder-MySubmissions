# パーツは円形で両端がくっついている
# つまり、手が重ならないようにした上で、何マス移動させるか
# なるべく短くなるように移動させたい
# 途中の操作の仕方は一意に決まると思う


N,Q=map(int,input().split())
Ring=[i+1 for i in range(N)]

l_pos=0
r_pos=1
step=0
for i in range(Q):
    H,T=input().split()
    T=int(T)-1

    # 手の移動させ方は一意に決まる
    # 移動の回数は2通りの差分の絶対値のうち、どちらか片方を採用する
    #  指定された手を基準点にとって考えr
    if H=='L':
        diff=0-l_pos
        l_pos=0
        r_pos=(r_pos+diff)%N
        T=(T+diff)%N
        if r_pos<T:
            # 左回りになる
            step+=(N-T)
        else:
            # 右回りになる
            step+=(T-l_pos)

        l_pos=(T-diff)%N
        r_pos=(r_pos-diff)%N
    elif H=='R':
        diff=0-r_pos
        r_pos=0
        l_pos=(l_pos+diff)%N
        T=(T+diff)%N
        if l_pos<T:
            # 左回りになる
            step+=(N-T)
        else:
            step+=(T-r_pos)%N
        
        r_pos=(T-diff)%N
        l_pos=(l_pos-diff)%N
print(step)



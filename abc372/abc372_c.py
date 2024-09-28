# 各クエリに対してO(log)で処理する必要がある
# SのX番の文字をCに置き換え、Sに文字列ABCが部分文字列として何箇所含まれるかを出力する
# 


N,Q=map(int,input().split())
S=list('..'+input()+'..')

c=0
for i in range(N+2):
    if S[i:i+3]==['A','B','C']:
        c+=1

for _ in range(Q):
    
    X,C=input().split()
    X=int(X)-1+2
    
    # X文字目を真ん中に含む5文字を調べれば十分
    # 置換前のX文字目の前後5文字を調べる
    for i in range(3):
        if S[X-2+i:X+1+i]==['A','B','C']:
            c-=1
    
    S[X]=C

    #置換後のX文字目の前後5文字を調べる 
    for i in range(3):
        if S[X-2+i:X+1+i]==['A','B','C']:
            c+=1
    
    print(c)
    
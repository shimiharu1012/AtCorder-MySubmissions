N,T=map(int,input().split())
Card=[[N*(i-1)+j for j in range(1,N+1)] for i in range(1,N+1)]
A=[int(a) for a in input().split()]

# 縦、横、斜めのラインに対して、カウンタを作る
# A_1~A_Tを調べ
# 対応するラインのカウンタをインクリメントする

row=[0]*N
col=[0]*N
d1,d2=0,0

ans=-1
for t in range(1,T+1):
    # iは行、jは列を表す
    # i,jは0~N-1
    i=(A[t-1]-1)//N
    j=(A[t-1]-1)%N

    # 各ラインのカウントをインクリメント
    row[i]+=1
    col[j]+=1
    if i==j:
        d1+=1

    if N-1-i==j:
        d2+=1
    


    if N in row:
        ans=t
        break
    elif N in col:
        ans=t
        break
    elif N==d1 or N==d2:
        ans=t
        break


print(ans)
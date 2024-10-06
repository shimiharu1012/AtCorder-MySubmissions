# 素朴には、N個からM個を選ぶ方法を調べれば良いので、
# NCMで求めることができる

# 基本的に、jに渡すお菓子はB_j以上の要素のうち最小のA_iを選べば良い
# したがって、ソートしたのち、Bを基準に探索する


N,M=map(int,input().split())
A=sorted([int(a) for a in input().split()])
B=sorted([int(b) for b in input().split()])


i=0
cost=0
for j in range(M):
    while i<N:
        if A[i]>=B[j]:
            cost+=A[i]
            i+=1
            break      
        else:
            i+=1
    
    if i==N:
        if j==M-1:
            # 最後の一人の場合
            # この場合においても、最後に見つからなかった場合がある
            if A[-1]<B[-1]:
                cost=-1
            break
        else:
            # まだ人が残っている場合
            cost=-1
            break

print(cost)


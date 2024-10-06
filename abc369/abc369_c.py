# 1-Nのうち、２つを選ぶ方法
# 素朴実装だとO(NxN/2)くらい

# lを選んだ時に、A[l:r+1]が等差数列であるようなrの最大値を求めれば良い
# したがって、2分探索でも求めることができる

# TLEするので、もう１工夫必要
# 小さい範囲から撮るのではなく、大きな範囲からとって、その部分列は確実に等差数列とする

N=int(input())
A=[int(a) for a in input().split()]


def cond(l,idx):
    # (l,idx)の区間で等差数列になるかを調べる
    if idx-l<2:
        return True
    
    # 要素が３つ以上の場合は、交差を調べる必要がある
    d=A[l+1]-A[l]
    for i in range(l,idx):
        if A[i+1]-A[i]!=d:
            return False
        
    return True
            

count=0
l=0
while l<N:
    ok=l
    ng=N
    
    while ok+1<ng:
        mid=(ok+ng)//2

        if cond(l,mid):
            ok=mid
        else:
            ng=mid

    r=ok
    # この時点で、(l,r)だけでなく、(l+1,r),(l+2,r-1)...なども全て等差数列となることが確定している
    # (l,r)の部分列の取り方は、組み合わせ的に計算で求めることができる
    count+=((r-l+1)+((r-l+1)*(r-l)//2))-1

    if r>l:
        l=r
    else:
        l+=1


print(count+1)
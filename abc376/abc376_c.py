# |A|=N |B|=N-1
# すべてのおもちゃが入るようにするために買い足す箱の最小の大きさを求める

# 今ある箱に対して、おもちゃを、一番ギリギリのサイズを選んで入れる

# 二分探索を使うっぽい
# 使えない箱が１つでもある時点でOUT

N=int(input())
A=sorted([int(a) for a in input().split()])
B=sorted([int(b) for b in input().split()])


def f():
    # must条件を調べる
    for i in range(N-1):
        if A[i]>B[i]:
            print(-1)
            return
    
    # 少なくとも、xは存在する
    # したがってxのうち最小のものを調べる
    # xの値は、必ずAの中に存在する
    for i in range(N-1,0,-1):
        if A[i]>B[i-1]:
            print(A[i])
            return
    
    print(A[0])
    return

f()
        
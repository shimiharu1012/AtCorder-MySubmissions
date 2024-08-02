N=int(input())
P=[int(p) for p in input().split()]
Q=int(input())

def f(A,B):
    for p in P:
        if p==A:
            return A
        if p==B:
            return B

    return -1

for i in range(Q):
    A,B=map(int,input().split())
    # 配列Pを先頭から舐めて
    # A,Bのうち、先に登場した方を出力する
    print(f(A,B))
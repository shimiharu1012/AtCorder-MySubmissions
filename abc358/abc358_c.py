from itertools import product

N,M=map(int,input().split())
S=[]
for i in range(N):
    s=input()
    S.append([True if s[j]=='o' else False for j in range(M)])

def f(N,M):
    MIN=N   # M種類のポップコーンを食べるために回る最小の店舗数
    for bit in product((0, 1), repeat=N):
        # M種類のポップコーンの有無をもつ配列
        is_popcorn=[False for _ in range(M)]
        for i in range(N):  # ONのbitに対応する店を調べる
            if bit[i]==1:   # i番目の店を訪れる
                is_popcorn=[is_popcorn[j] or S[i][j] for j in range(M)]
        
        if sum(is_popcorn)==M and sum(bit)<MIN:  # 全種類のポップコーンがあって、かつ店舗数が少なくなっていれば
            MIN=sum(bit)
    
    return MIN
                
print(f(N,M))
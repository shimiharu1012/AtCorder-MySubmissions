# 操作をl回施して得られる文字列をレベルlの文字列とする
# log210^18)<60
# したがって、もともとの文字列の長さ=1としても、レベル60の文字列まで調べれば十分
# レベルlの文字列のk文字目は、レベルl-1の文字列の何文字めかしらべ、
# これをレベル0になるまで再帰的に繰り返す

S=input()
Q=int(input())
K=map(int,input().split())



def f(k,l):
    if l==0:
        return S[k-1]
    h=len(S)*(2**(l-1))
    if k<=h:
        return f(k,l-1)
    return f(k-h,l-1).swapcase()


for k in K:
    print(f(k,60),end=" ")
print()
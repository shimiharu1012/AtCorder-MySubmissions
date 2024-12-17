# S[:i]==T[:i]となるiのうち最大のiを求める
# 二分探索で良い

S=input()+'.'
T=input()
N=len(T)
for i in range(N):
    if S[i]!=T[i]:
        print(i+1)
        break
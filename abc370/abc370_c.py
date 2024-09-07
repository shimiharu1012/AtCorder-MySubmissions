# 所定の操作を繰り返して、SをTにするための最小のもの
# 要素数最小のものが複数ある場合は、辞書順最小を返す
# 辞書順最小になるように操作を行うことが肝？



S=input()
T=input()
N=len(S)

from collections import deque

stack=deque()
X=[]
for i in range(N):
    if S[i]==T[i]:
        continue
    elif S[i]<T[i]:
        # i文字目は後回し
        stack.append(i)
    else:
        S=S[:i]+T[i]+S[i+1:]
        X.append(S)

while stack:
    i=stack.pop()
    S=S[:i]+T[i]+S[i+1:]
    X.append(S)


if len(X)==0:
    print(0)
else:
    print(len(X))
    print(*X,sep='\n')

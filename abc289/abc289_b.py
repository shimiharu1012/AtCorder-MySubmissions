# レ点が入ったタイミングでその文字をスタックする
# レ点がない場合、スタックが空なら文字を読む

from collections import deque

N,M=map(int,input().split())
A=[int(a) for a in input().split()]
nums=[i for i in range(1,N+1)]
IsReverse=[False]+[True if i in A else False for i in range(1,N+1)]
stack=deque()

ans=[]
for i in range(1,N+1):
    if IsReverse[i]:
        stack.append(i)
    else:
        ans.append(i)
        while stack:
            ans.append(stack.pop())

print(*ans)



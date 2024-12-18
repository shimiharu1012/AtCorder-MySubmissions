import collections

N=int(input())
A=[int(a) for a in input().split()]

stack=collections.deque()
length=0


# 連鎖によってボールが消えることは起こり得ない
for i in range(N):
    current_ball=A[i]

    if not stack:
        stack.append({'ball':current_ball,'count':1})
        length+=1
    else:
        if stack[-1]['ball']==current_ball:
            stack[-1]['count']+=1
            length+=1

            if stack[-1]['count']==current_ball:
                length-=stack.pop()['count']

        else:
            stack.append({'ball':current_ball,'count':1})
            length+=1


    print(length)
    

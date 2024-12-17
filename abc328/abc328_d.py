import collections

S=input()
N=len(S)

stack=collections.deque()
stack.append('#')
stack.append('#')
for i in range(N):
    stack.append(S[i])
    if stack[-3]=='A' and stack[-2]=='B' and stack[-1]=='C':
        stack.pop()
        stack.pop()
        stack.pop()

print(''.join(list(stack)[2:]))
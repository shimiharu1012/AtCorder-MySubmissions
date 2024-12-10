N,D=map(int,input().split())
S=input()

count=D
for i in range(N):
    if S[i]=='.':
        count+=1

print(count)
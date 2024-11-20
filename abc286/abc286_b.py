N=int(input())
S=input()
T=S[0]
for i in range(1,N):
    if S[i-1:i+1]=='na':
        T+='ya'
    else:
        T+=S[i]

print(T)
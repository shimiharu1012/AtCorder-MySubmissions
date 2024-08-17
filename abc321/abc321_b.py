N,X=map(int,input().split())
A=[int(a) for a in input().split()]
S=sorted(A)

# N-1ラウンド目までのスコアによって

ans=-1
# Nラウンド目で最高スコアを取る
for A_N in range(101):
    if A_N>S[-1]:
        R=sum(S)-S[0]
    elif A_N<S[0]:
        R=sum(S)-S[-1]
    else:
        R=sum(S)+A_N-S[-1]-S[0]
    
    if R>=X:
        ans=A_N
        break
    

print(ans)
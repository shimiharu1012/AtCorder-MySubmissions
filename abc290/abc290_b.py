# 予選通過の意思があるかつ順位がK以内

N,K=map(int,input().split())
S=input()
T=""
passes=0
i=0
while i<N:
    if S[i]=='o' and passes<K:
        passes+=1
        T+='o'
    else:
        T+='x'
    
    i+=1


print(T)
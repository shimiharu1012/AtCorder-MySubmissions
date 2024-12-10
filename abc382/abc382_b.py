N,D=map(int,input().split())
S='#'+input()

d=0
idx=N
while d<D: 
    while S[idx]==".":
        idx-=1
    S=S[:idx]+'.'*(N-idx+1)
    d+=1
print(S[1:])
N=int(input())
S=input()

count=0
for l in range(0,N-2):
    c=l+1
    r=l+2

    if S[l]==S[r]=='#' and S[c]=='.':
        count+=1

print(count)
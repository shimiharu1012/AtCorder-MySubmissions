# 26進数->10進数に変換すれば良い


S=input()
N=len(S)

ans=0
for i in range(N):
    ans+=(ord(S[-(i+1)])-ord('A')+1)*(26**i)

print(ans)


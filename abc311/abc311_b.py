# and演算を行えば良い
N,D=map(int,input().split())
ans=['o']*D

for i in range(N):
    S=list(input())
    ans=['o' if (ans[i]=='o' and S[i]=='o') else 'x'  for i in range(D)]

# print(ans)
seq_count=0
max_seq_count=0
for i in range(D):
    if ans[i]=='o':
        seq_count+=1
        if max_seq_count<seq_count:
            max_seq_count=seq_count
    else:
        seq_count=0

print(max_seq_count)
# 前から見ていけば十分　
# Kより短い連続部分列がなるべくできないようにする

N,K=map(int,input().split())
seq_list=input().split('X')
ans=0
for sub in seq_list:
    ans+=len(sub)//K

print(ans)

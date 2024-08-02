# 整数 Nが与えられます。

# 非負整数の組 (x,y,z) であって 
# x+y+z≤N を満たすものを辞書順で小さい方から順に全て出力してください。

N=int(input())
ans=[]
for x in range(N+1):
    for y in range(N+1-x):
        for z in range(N+1-x-y):
            ans.append([x,y,z])

for comb in ans:
    print(*comb,sep=' ')


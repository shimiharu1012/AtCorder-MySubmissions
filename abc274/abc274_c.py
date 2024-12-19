N=int(input())
A=['.']+[int(a) for a in input().split()]
gens=[0 for _ in range(2*N+2)]
# 観察記録をもとにアメーバの分裂を再現する
for i in range(1,2*N+2):
    if i==1:
        continue
    parent=A[i//2]
    gens[i]=gens[parent]+1

for gen in gens[1:]:
    print(gen)
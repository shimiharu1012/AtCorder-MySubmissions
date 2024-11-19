# 遡って探すのは効率が悪いので
# 値が登場するたびに、Bの候補を更新する

N=int(input())
A=['.']+[int(a) for a in input().split()]

B=[]
index_dict={}

for i in range(1,N+1):
    if not A[i] in index_dict:
        index_dict[A[i]]=[i]
        B.append(-1)
    else:
        B.append(index_dict[A[i]][-1])
        index_dict[A[i]].append(i)


print(*B)
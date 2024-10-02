from collections import deque

N=int(input())
A=[int(a) for a in input().split()]
row=deque()

for i in range(N):
    row.append(A[i])
    while True:        
        if len(row)==1:
            # 列にあるボールが1追加なので操作を終了
            break
        elif row[-1]!=row[-2]:    
            # 列にあるボールのうち右から1番目と2番目のものの大きさが異なる
            break
        else:
            l1=row.pop()
            l2=row.pop()
            row.append(l1+1)

# print(row)
print(len(row))
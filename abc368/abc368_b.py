# 整数型の入力
N=int(input())
A=[int(a) for a in input().split()]

def count_positive(A):
    return sum([(1 if a>0 else 0) for a in A ])


times=0
while count_positive(A)>1:
    A.sort(reverse=True)
    A[0]-=1
    A[1]-=1
    times+=1


print(times)
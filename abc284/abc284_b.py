def count_odd_num(X):
    count=0
    for x in X:
        if x%2==1:
            count+=1
    
    return count

T=int(input())
ans=[]
for i in range(T):
    N=int(input())
    A=[int(a) for a in input().split()]
    print(count_odd_num(A))

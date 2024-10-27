
N=int(input())
A=[int(a) for a in input().split()]
new_A=[]
for i in range(N-1):
    new_A.append(A[i])
    if A[i]+1<A[i+1]:
    
        add=A[i]+1
        while add<A[i+1]:
            new_A.append(add)
            add+=1
    elif A[i]-1>A[i+1]:
        add=A[i]-1
        while add>A[i+1]:
            new_A.append(add)
            add-=1
    else:
        pass

    # new_A.append(A[i+1])
new_A.append(A[-1])
print(*new_A)
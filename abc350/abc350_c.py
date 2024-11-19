N=int(input())
A=[0]+[int(a) for a in input().split()]
op=[]


def f():
    K=0
    for i in range(1,N+1):
        while A[i]!=i:
            if K>=N-1:
                return K
            j=A[i]
            
            A[i],A[j]=A[j],A[i]
            K+=1
            op.append((min(i,j),max(i,j)))

    return K

K=f()
print(K)
for o in op:
    print(o[0],o[1])


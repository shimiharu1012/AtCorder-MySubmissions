N=int(input())
A=[0]+[int(a) for a in input().split()]
Q=int(input())
for i in range(Q):
    query=input().split()
    
    if query[0]=='1':
        k=int(query[1])
        x=int(query[2])
        A[k]=x
    elif query[0]=='2':
        k=int(query[1])
        print(A[k])
    else:
        pass




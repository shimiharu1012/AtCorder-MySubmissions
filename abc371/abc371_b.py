N,M=map(int,input().split())
HaveKids=[False for i in range(N+1)]
IsTaro=[False for i in range(M)]
for i in range(M):
    A_B=input().split()
    A=int(A_B[0])
    B=A_B[1]
    if (not HaveKids[A]) and (B=='M'):
        HaveKids[A]=True
        IsTaro[i]=True
    else:
        pass

for i in range(M):
    if IsTaro[i]:
        print("Yes")
    else:
        print("No")
        


    
    


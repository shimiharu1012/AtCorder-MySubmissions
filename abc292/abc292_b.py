N,Q=map(int,input().split())
player=[0]*(N+1)

for i in range(Q):
    c,x=input().split()

    if c=='1':
        player[int(x)]+=1
    elif c=='2':
        player[int(x)]+=2
    else:
        if player[int(x)]>=2:
            print("Yes")
        else:
            print("No")
        
    


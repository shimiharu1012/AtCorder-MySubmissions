def spend_turn(T,hp):
    if T%3==0:
        if hp%5==1:
            return (hp//5)*3+1
        elif hp%5==2:
            return (hp//5)*3+2
        else:
            return -(-hp//5)*3
    elif T%3==1:
        if hp%5==1:
            return (hp//5)*3+1
        elif hp%5==0:
            return (hp//5)*3    
        else:
            return (hp//5)*3+2
    elif T%3==2:
        if hp%5==4:
            return (hp//5)*3+2
        elif hp%5==0:
            return (hp//5)*3
        else:
            return (hp//5)*3+1



N=int(input())
H=[int(a) for a in input().split()]
T=0
for i in range(N):
   T+=spend_turn(T,H[i])

print(T) 


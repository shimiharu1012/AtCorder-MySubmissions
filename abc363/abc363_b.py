t=0
N,T,P=map(int,input().split())
L=[int(l) for l in input().split()]
while True:
    if sum(True if l>=T else False for l in L)>=P:
        print(t)
        break
    else:
        t+=1
        L=[l+1 for l in L]
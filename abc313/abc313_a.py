N=int(input())
P=[int(p) for p in input().split()]

if N==1:
    print(0)
else:
    if P[0]<max(P[1:]):
        print(max(P[1:])-P[0]+1)
    elif P[0]==max(P[1:]):
        print(1)
    else:
        print(0)

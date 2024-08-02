# N<=10^18
# x+y<100　程度
# したがってx,y

N=int(input())


def f(N):
    x=0
    X=1
    while x<100:
        y=0
        Y=1
        while y<100:
            # print(X*Y)
            if X*Y==N:
                return True
            Y*=3
            y+=1
        
        X*=2
        x+=1
    return False


if f(N):
    print("Yes")
else:
    print("No")
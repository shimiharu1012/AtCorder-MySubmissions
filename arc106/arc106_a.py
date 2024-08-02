# A,Bはそれぞれlog3_N,log5_N以下
# したがって組み合わせの数は高々(log3_N*log5_N)
from math import log
N=int(input())

def f(N):    
    A_max=int(log(N,3))
    B_max=int(log(N,5))

    for i in range(1,A_max+2):
        for j in range(1,B_max+2):
            if 3**i+5**j==N:
                return [i,j]
    
    return -1

ans=f(N)
if ans==-1:
    print(-1)
else:
    print(*ans)
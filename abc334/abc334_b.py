A,M,L,R=map(int,input().split())

# L<=A+MKを満たす最小のK:Kmin
# A+MK<=Rを満たす最大のK：Kmax

# 床関数
def my_floor(a,b):
    return a//b
# 天井関数
def my_ceil(a,b):
    return -(-a//b)



Kmin=my_ceil(L-A,M)
Kmax=my_floor(R-A,M)

print(Kmax-Kmin+1)


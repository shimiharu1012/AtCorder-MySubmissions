# 貪欲方だと10^20通りでTLE
# Mの値に着目する？
# M=3^aの時、Ai<aでなくてはならない
# 従って、a^20通りまで削減可能
import math

M=int(input())


N=0
A=[]
while True:
    a=int(math.log(M,3))
    M-=3**a
    A.append(a)
    N+=1

    if M<=0:
        break

print(N)
print(*A)


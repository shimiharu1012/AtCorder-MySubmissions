N=int(input())
A=sorted([int(a) for a in input().split()])

idx=0
A_i=A[idx]

while True:
    if not A_i in A:
        print(A_i)
        break
    A_i+=1



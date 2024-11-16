N,M=map(int,input().split())
A=[int(a) for a in input().split()]
B=[int(b) for b in input().split()]

C=sorted(A+B)
set_A=set(A)
set_B=set(B)

ans_A=[]
ans_B=[]
for i in range(N+M):
    if C[i] in set_A:
        ans_A.append(i+1)
    else:
        ans_B.append(i+1)


print(*ans_A)
print(*ans_B)
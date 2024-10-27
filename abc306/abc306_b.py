A=[int(a) for a in input().split()]
total=0

for i in range(len(A)):
    total+=A[i]*(2**i)

print(total)
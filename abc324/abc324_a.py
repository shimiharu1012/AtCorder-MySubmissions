N=int(input())
A=[int(a) for a in input().split()]

def f():
    for i in range(N-1):
        if A[i]!=A[i+1]:
            return False
    
    return True


if f():
    print("Yes")
else:
    print("No")
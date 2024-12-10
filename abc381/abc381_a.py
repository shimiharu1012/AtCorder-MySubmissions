N=int(input())
S=input()

def f():
    if N%2==0:
        return False
    
    for i in range(N):
        if i<N//2 and S[i]!='1':
            return False
        elif i==N//2 and S[i]!='/':
            return False
        elif i>N//2 and S[i]!='2':
            return False
    
    return True

if f():
    print("Yes")
else:
    print("No")
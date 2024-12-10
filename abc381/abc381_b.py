S=input()
N=len(S)
history=set()

def f():
    if N%2==1:
        return False
    
    
    for i in range(N//2):
        if S[2*i] in history:
            return False
        elif S[2*i]!=S[2*i+1]:
            return False
        else:
            history.add(S[2*i])
    return True

if f():
    print("Yes")
else:
    print("No")
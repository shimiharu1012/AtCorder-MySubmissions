S=input()

def f():
    for i in range(len(S)):
        if i==0 :
            if S[i].islower():
                return False
        else:
            if not S[i].islower():
                return False
            
    return True

print("Yes" if f() else "No")
        
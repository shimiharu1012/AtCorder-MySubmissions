N=int(input())

def OK():
    flag=0
    for i in range(N-1):
        
        if input()=='sweet':
            flag+=1
        else:
            flag=0

        if flag==2:
            return False

    return True

print("Yes" if OK() else "No")



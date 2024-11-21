def rotate(X):
    N=len(X)
    X_rotated=[[0 for i in range(N)] for j in range(N)]
    for i in range(N):
        for j in range(N):
            X_rotated[N-j-1][i]=X[i][j]
    
    return X_rotated

def condition(X,Y):
    N=len(X)
    for i in range(N):
        for j in range(N):
            if X[i][j]==1 and Y[i][j]==0:
                return False
            
    return True

N=int(input())
A=[]
B=[]


for i in range(N):
    A.append([int(a) for a in input().split()])


for i in range(N):
    B.append([int(b) for b in input().split()])

ans="No"

rotation=0
while rotation<360:
    if condition(A,B):
        ans="Yes"
        break
    
    A=rotate(A)
    rotation+=90

print(ans)
    
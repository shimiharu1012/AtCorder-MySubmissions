import math

def distance(p1,p2):
    d=math.sqrt((p1[0]-p2[0])**2+(p1[1]-p2[1])**2)
    return d

N=int(input())

# X1,Y1=map(int,input().split())
Cx=0
Cy=0
total_d=0
for i in range(N):
    X,Y=map(int,input().split())
    total_d+=distance([Cx,Cy],[X,Y])
    
    Cx=X
    Cy=Y

total_d+=distance([Cx,Cy],[0,0])

print(total_d)
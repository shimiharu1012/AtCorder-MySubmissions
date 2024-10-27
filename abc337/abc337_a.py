N=int(input())
X_sum=0
Y_sum=0
for i in range(N):
    X,Y=map(int,input().split())
    X_sum+=X
    Y_sum+=Y

if X_sum>Y_sum:
    print("Takahashi")
elif X_sum<Y_sum:
    print("Aoki")
else:
    print("Draw")
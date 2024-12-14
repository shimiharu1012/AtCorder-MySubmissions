N=int(input())
S=input()

# "の個数が偶数->"の奇数個め
T=""
count=1
for i in range(N):
    if count%2==1 and S[i]==",":
        T+="."
    elif S[i]=='"':
        count+=1
        T+=S[i]
    else:
        T+=S[i]

print(T)
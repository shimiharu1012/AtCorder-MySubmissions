S=input()

cond1=False
cond2=False


temp=0
for i in range(len(S)):
    if S[i]=='B':
        temp+=i

cond1=(temp%2==1)

temp2=[]
for i in range(len(S)):
    if S[i]=='K' or S[i]=='R':
        temp2.append(S[i])

cond2=(temp2==['R','K','R'])


if cond1 and cond2:
    print("Yes")
else:
    print("No")
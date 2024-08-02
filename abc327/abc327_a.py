N=int(input())
S=input()

ans='No'
for i in range(N-1):
    if (S[i]=='a' and S[i+1]=='b') or (S[i]=='b' and S[i+1]=='a'):
        ans='Yes'
        break

print(ans)
    
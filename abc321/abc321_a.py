N=input()

ans=True
for i in range(len(N)-1):
    if int(N[i])>int(N[i+1]):
        pass
    else:
        ans=False
        break

print("Yes" if ans else "No")
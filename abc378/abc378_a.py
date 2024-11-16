A=[int(a) for a in input().split()]
ans=0
for num in range(1,5):
    ans+=A.count(num) //2

print(ans)
A,B,C=map(int,input().split())

now=B
ans="Yes"
while now!=C:
    if now==A:
        ans="No"
        break
    
    now=(now+1)%24

print(ans)
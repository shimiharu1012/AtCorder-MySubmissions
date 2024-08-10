# Q<=200000
# x <1000000


balls={}

ans=0
Q=int(input())

for i in range(Q):
    query=input().split()
    op=int(query[0])

    if op==1:
        x=int(query[1])
        if x not in balls or balls[x]==0:
            balls[x]=1
            ans+=1
        else:
            balls[x]+=1
    elif op==2:
        x=int(query[1])
        balls[x]-=1
        if balls[x]==0:
            ans-=1
    elif op==3:
        print(ans)
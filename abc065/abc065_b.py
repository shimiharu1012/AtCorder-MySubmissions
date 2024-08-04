N=int(input())
A=[-1]
visited=[False]*(N+1)
for i in range(N):
    A.append(int(input()))



pushed=[False]*(N+1)
times=0
now=1
while True:

    now=A[now]
    times+=1
    if now==2:
        print(times)
        break
    elif pushed[now]:
        print(-1)
        break

    pushed[now]=True


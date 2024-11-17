N=int(input())
S=input()
point=(0,0)
visited_point=set()
visited_point.add(point)

for i in range(N):
    if S[i]=='R':
        point=(point[0]+1,point[1])
    elif S[i]=='L':
        point=(point[0]-1,point[1])
    elif S[i]=='U':
        point=(point[0],point[1]-1)
    elif S[i]=='D':
        point=(point[0],point[1]+1)
    
    if not point in visited_point:
        visited_point.add(point)

if len(visited_point)==N+1:
    print("No")
else:
    print("Yes")
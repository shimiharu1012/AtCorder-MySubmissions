M,D=map(int,input().split())
y,m,d=map(int,input().split())

if m==M and d==D:
    # 大晦日->元日
    print(y+1,1,1)
elif d==D:
    print(y,m+1,1)
else:
    print(y,m,d+1)
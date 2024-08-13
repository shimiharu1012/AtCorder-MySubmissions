N,T,A=map(int,input().split())
# 未開票の票数
remain=N-T-A
# 票数の差
diff=abs(T-A)

if remain<diff:
    print("Yes")
else:
    print("No")
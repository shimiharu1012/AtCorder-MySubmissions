# 整数型の入力
M=int(input())
D=[int(d) for d in input().split()]
mid_day=(sum(D)+1)//2

m=1
for dpm in D:
    if mid_day>dpm:
        m+=1
        mid_day-=dpm
    else:
        break

print(m,mid_day)


# D1+D2+...D_M+1//2==1


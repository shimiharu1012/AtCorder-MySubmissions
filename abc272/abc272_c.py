N=int(input())
A=[int(a) for a in input().split()]
odd=sorted([Ai for Ai in A if Ai%2==1])
even=sorted([Ai for Ai in A if Ai%2==0])
# 奇数2つor偶数2つがあれば良い
# 偶数の作り方は　奇+奇　or 偶+偶

if len(odd)>=2 and len(even)>=2:
    print(max(odd[-1]+odd[-2],even[-1]+even[-2]))
elif len(odd)>=2:
    print(odd[-1]+odd[-2])
elif len(even)>=2:
    print(even[-1]+even[-2])
else:
    # 奇数、偶数ともに1つ以下
    print(-1)


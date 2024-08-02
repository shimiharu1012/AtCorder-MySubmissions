N,K=map(int,input().split())

# リストに入っている方を足して全体から引く
# 仮に1-Kが全てAに含まれてるとすると、1+2+3+...2*10^9
# 足し算を大量にすることになる
sum=K*(K+1)//2
A=set([int(a) for a in input().split()])
for a in A:
    if 1<=a and a<=K:
        sum-=a

print(sum)
# A1,A2...AN, A1, A2...
# 和がsとなる部分があるかを調べる
# A1+..Anの和を基準として考える
# 累積和として部分列も保持しておく

N,S=map(int,input().split())
A=[int(a) for a in input().split()]
acm_sums=[0]
for i in range(N):
    acm_sums.append(acm_sums[-1]+A[i])

acm_sums_set=set(acm_sums)
diff1=S-acm_sums[N]*(S//acm_sums[N])
diff2=-(S-acm_sums[N]*(S//acm_sums[N]+1))
# 累積和の差分を全て調べる
# diff1かdiff2のどちらかに一致したらYes
for i in range(N+1):
    if acm_sums[i]+diff1 in acm_sums_set or acm_sums[i]+diff2 in acm_sums_set:
        print("Yes")
        break

    if i==N:
        print("No")

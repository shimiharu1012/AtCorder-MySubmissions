N,L,R=map(int,input().split())

nums=[i for i in range(1,N+1)]
print(*(nums[:L-1]+sorted(nums[L-1:R],reverse=True)+nums[R:]))

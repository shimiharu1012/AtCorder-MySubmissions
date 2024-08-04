# 範囲 1-10^12-1
# 条件 前後一致 (11,22,33...999999_999999)

# 条件について、範囲に含まれるかを考える
N=int(input())
count=0

for i in range(1,1000000):
    x=int(str(i)+str(i))
    if x<=N:
        count+=1
    elif x>N:
        break
print(count)
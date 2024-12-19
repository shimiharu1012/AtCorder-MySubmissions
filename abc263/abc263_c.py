# 長さ3で1以上5以下の場合
# 1 2 3
# 1 2 4
# 1 2 5
# 2 3 4
# ...
# 3 4 5

# 辞書順で列挙する→DFS
# back trackすることを忘れずに

N,M=map(int,input().split())


def is_monoincrease(array):
    n=len(array)
    for i in range(n-1):
        if array[i+1]-array[i]<=0:
            return False
    
    return True



def dfs(array):
    # 関数の中で、すでにarrayの条件を満たさない
    # すなわち単調増加になり得ないものを弾きたい
    if not is_monoincrease(array):
        return
    
    if len(array)==N:
        all_arrays.append(array)
    
    a_min=array[-1]+1
    a_max=M
    
    for a_i in range(a_min,a_max+1):
        dfs(array+[a_i])
    

all_arrays=[]

for i in range(1,M+1):
    dfs([i])

for array in all_arrays:
    print(*array)

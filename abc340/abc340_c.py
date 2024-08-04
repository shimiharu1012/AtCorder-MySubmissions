# どの順番で操作しても結果は同じ
# ただし、でかい数字から順番に取り出していったら時間がめちゃくちゃかかる
# 

import math
from functools import lru_cache
# sys.setrecursionlimit=1000000

N=int(input())
# numsは2以上の整数
# 操作を行う条件は2以上の整数があること
nums=set()

total=0

@lru_cache(maxsize=None)
def rec(x):
    # 黒板に整数xが１つ書かれているとき
    # 操作を行えなくなるまでに払う金額の総和
    if x<2:
        return 0
    elif x%2==0:
        return    x+2*rec(x//2)
    else:
        return x+rec(x//2)+rec((x+1)//2)


print(rec(N))
N=int(input())

# N=345->343
# N=6 -> 1

# 回文になる整数から探すか
# Nが大きければ組み合わせがとても大きくなりそう

# 回文かどうかを調べる
def is_palindrome(s):
    '''文字列sが回文かどうかを判定する'''
    for i in range(len(s)//2):
        if s[i]!=s[-(i+1)]:
            return False
    
    return True


# 立方数をから探すか
def f(N):
    ret=-1
    x=1
    while (x**3<=N):
        K=x**3
        if is_palindrome(str(K)):
            ret=K
        x+=1

    return ret

print(f(N))
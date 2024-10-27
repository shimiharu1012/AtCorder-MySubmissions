def is_palindrome_2(s):
    '''文字列sが回文かどうかを判定する ver2'''
    # s[::-1]はsの回文
    return s==s[::-1]



N=int(input())
S=[]
for i in range(N):
    S.append(input())

def f():
    for i in range(N):
        for j in range(N):
            if i==j:
                continue

            if is_palindrome_2(S[i]+S[j]):
                return True
    
    return False

print("Yes" if f() else "No")

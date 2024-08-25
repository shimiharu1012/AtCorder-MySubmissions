# 整数型の入力
X=input()

def f():
    if X[-1]!='0':
        return X
    
    if X[-2]!='0':
        return X[:-1]    
    
    if X[-3]!='0':
        return X[:-2]

    return X[:-4]


print(f())

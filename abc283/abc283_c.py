# ボタンを押すために必要な最小回数を求める
# 逆操作で最短で０にする方法を考える

# 
S=input()

times=0
while S!='0':
    
    if len(S)==1:
        times+=1
        S='0'
    elif S[-1]!='0':
        times+=1
        S=S[:-1]
    elif S[-2]!='0':
        times+=1
        S=S[:-1]
    elif S[-2]=='0':
        times+=1
        S=S[:-2]

print(times)    
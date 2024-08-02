# Sの長さ3の部分文字列(連続とは限らない)
# Sの長さ2の部分文字列（連続とは限らない）の末尾にXを追加したもの
# Tになるものがあるかを調べる

# 初めにTにXが含まれているかを調べる
# Xが含まれていることは弱い条件なので問題ない

# Sは長い文字列
S=input()
T=input().lower()
idx=0
for s in S:
    if s==T[idx]:
        idx+=1
    
    if idx==3:
        break

if idx==3 or (idx==2 and T[-1]=='x'):
    print("Yes")
else:
    print("No")
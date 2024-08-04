N,X,Y=map(int,input().split())

# N<=2*10^5
A=[int(a) for a in input().split()]
B=[int(b) for b in input().split()]

# 範囲：全ての料理の順番
# 条件：甘さの合計<=X かつ　しょっぱさの合計<=Y

# 求めるもの
# 食べる料理の最小個数
# 甘さの合計が>X または　しょっぱさの合計が＞Yとなる

A=sorted(A,reverse=True)
B=sorted(B,reverse=True)

x=0
y=0
for i in range(N):
    x+=A[i]
    y+=B[i]

    if x>X or y>Y:
        print(i+1)
        break

if i==N-1:
    print(N)




S=input()

# 文字列を循環させて考えれば良い
# 前後が違う文字に挟まれる＝一文字のやつ
N=len(S)
for i in range(N):
    if S[i-1]!=S[i] and S[i]!=S[(i+1)%N]:
        print(i+1)
        break
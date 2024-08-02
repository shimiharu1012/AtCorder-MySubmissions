# クエリ形式
# １問ずつ答える
# 計算量を削減するために何か工夫が必要？

N,Q=map(int,input().split())
S=input()

# 1文字目からr文字目までで隣り合う部分の個数を求める
# これを累積和として扱い、計算量を減らす
A=[0]
count=0
for p in range(N-1):
    if S[p]==S[p+1]:
        count+=1
    A.append(count)


# クエリを処理
for q in range(Q):
    l,r=map(int,input().split())
    print(A[r-1]-A[l-1])
N=int(input())
D=[0]+[int(d) for d in input().split()]

# 1年＝Nヶ月
# i月はD_i日
# 1年のうちゾロ目になる日付の日数

# 月と日数の文字列が全て一種類の文字からなる場合
# ゾロ目の日付

# ゾロ目かどうかを判定する
def is_same_numbers(s):
    for i in range(len(s)-1):
        if s[i]!=s[i+1]:
            return False
    return True


count=0
for month in range(1,N+1):
    for date in range(1,D[month]+1):
        if is_same_numbers(str(month)+str(date)):
            count+=1

print(count)
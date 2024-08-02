write_count=0
div=10**9+7
L,R=map(int,input().split())

# forのループ数も大きい
# 群数列の和として計算する？

# L->min(Lと同じ桁数の最大値,R)までを足す
# この処理を,Rに達するまで繰り返す
# つまり、for文はO(Rの桁数)程度の計算量でおさまる
d_L=len(str(L))
d_R=len(str(R))
d=d_L
write_count=0
while True:
    if d_L<d_R:
        # L+...Lと同じ桁数の最大整数
        add=((d_L*(10**d_L-L)*(10**d_L-1+L))//2)%div
        write_count=(write_count+add)%div
        L=10**d_L
        d_L+=1
    else:
        add=((d_L*(R-L+1)*(R+L))//2)%div
        write_count=(write_count+add)%div
        break

print(write_count)
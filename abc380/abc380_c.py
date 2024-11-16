# よりシンプルに考えれば、これはK-1個目のあとの0の塊を取り出して
# K個目の1の塊の後ろにくっつけることに等しい


N,K=map(int,input().split())
S=input()



before='0'
blocks=0
i=0
l,r,be=0,0,0
while i<N:
    if before=='0' and S[i]=='1':
        blocks+=1
    

    # K-1ブロック目の次の0のインデックス
    if blocks==K-1 and before=='1' and S[i]=='0':
        l=i

    # Kブロック目の前の0のインデックス
    if blocks==K and before=='0' and S[i]=='1':
        r=i-1

    # Kブロック目の1の塊の最後のインデックス
    if blocks==K and S[i]=='1':
        if i==N-1:
            be=i
        elif S[i+1]=='0':
            be=i
        
    
    before=S[i]
    
    i+=1

print(S[:l]+S[r+1:be+1]+S[l:r+1]+S[be+1:])
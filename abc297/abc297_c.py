# 行ごとにみる
# 左づめで問題ない


H,W=map(int,input().split())
Map=[]
for i in range(H):
    row=input()+'.'
    new_row=""
    j=0
    while j<W:
        if row[j]=='T' and row[j+1]=='T':
            new_row+="PC"
            j+=2
        else:
            new_row+=row[j]
            j+=1
        
    Map.append(new_row)


print(*Map,sep='\n')

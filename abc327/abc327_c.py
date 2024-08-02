# 与えられた9*9行列がナンプレになっているか

A=[]
for i in range(9):
    A.append([int(a) for a in input().split()])

# サイズ固定なので、行、列、ブロックを全て調べて
# 計算は十分間に合う

# 行のリスト
rows=A[:]
# 列のリスト
cols=[]
for j in range(9):
    col=[A[i][j] for i in range(9)]
    cols.append(col)
# ブロックのリスト
blocks=[]
for b in range(9):
    
    i=3*(b%3)
    j=3*(b//3)
    # print(i,j)
    block=rows[i][j:j+3]+rows[i+1][j:j+3]+rows[i+2][j:j+3]
    blocks.append(block)


# print(*rows,sep='\n')
# print()
# print(*cols,sep='\n')
# print()
# print(*blocks,sep='\n')

def is_number_place():

    # まずは行について調べる
    for row in rows:
        if set(row)!=set(list(range(1,10))):
            return False

    # 次に列について調べる
    for col in cols:
        if set(col)!=set(list(range(1,10))):
            return False
        
    # 次にブロックについて調べる
    for block in blocks:
        if set(block)!=set(list(range(1,10))):
            return False
            

    return True


print("Yes" if is_number_place() else "No")
    

    
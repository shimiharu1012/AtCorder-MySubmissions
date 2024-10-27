# 十字路に交差しない点がいくつあるかを調べる
# 縦列をor演算で足していって、おける列を調べて、
# 行を見ていって、おける行を調べる

ok_col=[1]*8
ok_row=0
for i in range(8):
    Si=input()
    ok_col=[1 if Si[i]=='.' and ok_col[i]==1 else 0 for i in range(8)]

    if not '#' in Si:
        ok_row+=1


print(ok_row*sum(ok_col))
# 素朴な実装
# 点の対を順不同なsetとして持って
# 距離が等しい点対のリストに入っているかを比較する

group1=[['A','B'],['B','C'],['C','D'],['D','E'],['E','A']]
group2=[['A','C'],['A','D'],['B','D'],['B','E'],['C','E']]

group1=[set(list) for list in group1]
group2=[set(list) for list in group2]

s1_s2=input()
s1=s1_s2[0]
s2=s1_s2[1]


t1_t2=input()
t1=t1_t2[0]
t2=t1_t2[1]

if (set([s1,s2]) in group1 and set([t1,t2]) in group1)\
    or (set([s1,s2]) in group2 and set([t1,t2]) in group2):
    
    print("Yes")
else:
    print("No")
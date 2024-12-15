names = [
    "A",
    "B",
    "C",
    "D",
    "E",
    "AB",
    "AC",
    "BC",
    "AD",
    "BD",
    "AE",
    "CD",
    "BE",
    "CE",
    "DE",
    "ABC",
    "ABD",
    "ACD",
    "ABE",
    "BCD",
    "ACE",
    "BCE",
    "ADE",
    "BDE",
    "CDE",
    "ABCD",
    "ABCE",
    "ABDE",
    "ACDE",
    "BCDE",
    "ABCDE"
]




a,b,c,d,e=map(int,input().split())
p_n_list=[]
for name in names:
    point=0
    if 'A' in name:
        point+=a
    
    if 'B' in name:
        point+=b
    if 'C' in name:
        point+=c
    if 'D' in name:
        point+=d
    if 'E' in name:
        point+=e
    
    
    p_n_list.append([name,point])

ans1=sorted(p_n_list,key=lambda x:(-x[1],x[0]))
for item in [item[0] for item in ans1]:
    print(item)
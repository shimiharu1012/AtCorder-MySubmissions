# 一致or反転一致は同じものとみなす



N=int(input())
S=set()
for i in range(N):
    Si=input()
    if Si in S  or Si[::-1] in S:
        pass
    else:
        S.add(Si)
    
print(len(S))
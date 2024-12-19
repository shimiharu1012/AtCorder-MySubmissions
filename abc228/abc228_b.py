N,X=map(int,input().split())

#　iは情報元,Aiは情報先 
# 1->1 or 0
A=['']+[int(a) for a in input().split()]

# 情報先がいなくなるまで数珠繋ぎで伝達する
knows=set([X])

while True:
    if A[X] in knows:
        break
    knows.add(A[X])
    X=A[X]
    

print(len(knows))

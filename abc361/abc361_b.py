# x,y,z座標の区間が全て交わっていればOK
# 1つでも交わっていないとNG

def is_intersection(l1,u1,l2,u2):
    # 一次元の座標区間において、
    # 共通部分があるかを調べる
    return l2<u1 and l1<u2


A=list(map(int,input().split()))
B=list(map(int,input().split()))

if is_intersection(min(A[0],A[3]),max(A[0],A[3]),min(B[0],B[3]),max(B[0],B[3]))\
    and is_intersection(min(A[1],A[4]),max(A[1],A[4]),min(B[1],B[4]),max(B[1],B[4]))\
    and is_intersection(min(A[2],A[5]),max(A[2],A[5]),min(B[2],B[5]),max(B[2],B[5])):

    print("Yes")
else:
    print("No")

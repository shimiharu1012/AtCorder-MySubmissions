H,W=map(int,input().split())
A=[]
B=[]


for i in range(H):
    A.append(list(input()))

for i in range(H):
    B.append(list(input()))


# シフトの順番は関係ない
# マップは十分小さいので、前通り試しても十分間に合う

def x_shift(map):
    map_shift=[]
    for i in range(H):
        map_shift.append([map[i][-1]]+map[i][:-1])

    return map_shift


def y_shift(map):
    map_shift=[]
    for j in range(H):
        if j==0:
            map_shift.append(map[-1])
        else:
            map_shift.append(map[j-1])

    return map_shift



def f():
    A_shift=A[:]
    for y in range(H):
        # 縦に1つずらす
        A_shift=y_shift(A_shift)
        for x in range(W):
            A_shift=x_shift(A_shift)
            if A_shift==B:
                return True
    
    return False

if f():
    print("Yes")
else:
    print("No")
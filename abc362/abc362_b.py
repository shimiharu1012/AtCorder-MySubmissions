# ３点の座標
# 直角三角形か否か

# 三角形か判定する
# 3点が同一直線上に並ばない
def is_triangle(a,b,c):
    vec1=[b[0]-a[0],b[1]-a[1]]
    vec2=[c[0]-a[0],c[1]-a[1]]

    if vec1[0]!=0 and vec2[0]!=0:
        if (vec1[1]/vec1[0])==(vec2[1]/vec2[0]):
            return False
        else:
            return True
    elif vec1[0]!=0 or vec2[0]!=0:
        return True
    else:
        return False


def is_right_triangle(a,b,c):
    if not is_triangle(a,b,c):
        return False
    
    A=(a[0]-b[0])**2+(a[1]-b[1])**2
    B=(b[0]-c[0])**2+(b[1]-c[1])**2
    C=(c[0]-a[0])**2+(c[1]-a[1])**2

    if max(A,B,C)==A+B+C-max(A,B,C):
        return True
    else:
        return False
    
a=[int(x) for x in input().split()]
b=[int(x) for x in input().split()]
c=[int(x) for x in input().split()]

if is_right_triangle(a,b,c):
    print("Yes")
else:
    print("No")
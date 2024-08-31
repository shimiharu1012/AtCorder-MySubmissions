D=int(input())

_min=D
for x in range(0,int(D**0.5)+1):
    z=D-x**2  # zが負になることはないはず
    if z<0:
        diff=abs(z)
    else:
        y_lb=int(z**0.5)
        y_ub=y_lb+1
        diff=min(abs(z-y_lb**2),abs(z-y_ub**2))
    
    if diff<_min:
            _min=diff


print(_min)
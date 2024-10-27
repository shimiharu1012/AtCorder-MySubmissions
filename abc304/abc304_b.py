N=input()
if int(N)<10**3:
    print(N)
else:
    d=len(N)
    print((int(N)//10**(d-3))*(10**(d-3)))
# elif N<10**4:
#     print(N//10)
# elif N<10**5:

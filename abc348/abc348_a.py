N=int(input())
last=''
for i in range(1,N+1):
    if i==N:
        last='\n'
    if i%3==0:
        print('x',end=last)
    else:
        print('o',end=last)
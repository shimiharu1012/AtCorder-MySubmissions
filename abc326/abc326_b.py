N=int(input())

n=N
while True:
    tmp=n
    a=tmp//100
    b=(tmp%100)//10
    c=tmp%10

    if a*b==c:
        break
    else:
        n+=1

print(n)
    
N,M,P=map(int,input().split())
d=M
count=0
while True:
    if d>N:
        break

    count+=1
    d+=P

print(count)
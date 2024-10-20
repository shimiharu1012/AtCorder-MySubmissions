N,C=map(int,input().split())
T=[int(t) for t in input().split()]

get_candy=T[0]
count=1

for i in range(1,N):
    if T[i]-get_candy>=C:
        get_candy=T[i]
        count+=1

print(count)


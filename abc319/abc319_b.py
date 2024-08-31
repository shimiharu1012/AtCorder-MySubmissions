N=int(input())

# d=[x for x in range(1,10) if N%x==0]
# print(d)

S=''
for i in range(N+1):
    s_i='-'
    for j in range(1,10):
        if N%j==0 and i%(N//j)==0:
            s_i=str(j)
            break
    
    S+=s_i

print(S)

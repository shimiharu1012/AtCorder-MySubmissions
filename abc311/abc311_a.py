N=int(input())
S='.'+input()

abc=set()
for i in range(1,N+1):
    abc.add(S[i])
    if len(abc)==3:
        print(i)
        break

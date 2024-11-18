N,K=map(int,input().split())
name_list=[]
for i in range(N):
    name_list.append(input())

print(*sorted( name_list[:K]),sep='\n')
# N<=100なので、組み合わせの総数は小さい
# したがって、単純に全探索
import math
N,S,M,L=map(int,input().split())

min_cost=10000*20
for s_num in range(0,(N//6)+2):
    
    for m_num in range(0,(N//8)+2):
        
        for l_num in range(0,(N//12)+2):

            eggs=s_num*6+m_num*8+l_num*12
            cost=s_num*S+m_num*M+l_num*L

            if eggs>=N and cost<min_cost:
                min_cost=cost


print(min_cost)
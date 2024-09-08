N=int(input())


L_pos=[]
R_pos=[]
for i in range(N):
    A_S=input().split()
    A=int(A_S[0])
    S=A_S[1]

    if S=='L':
        L_pos.append(A)
    elif S=='R':
        R_pos.append(A)

fatigue=0
if len(L_pos)>=2:
    fatigue+=sum([abs(L_pos[i+1]-L_pos[i]) for i in range(len(L_pos)-1)])

if len(R_pos)>=2:
    fatigue+=sum([abs(R_pos[i+1]-R_pos[i]) for i in range(len(R_pos)-1)])

print(fatigue)


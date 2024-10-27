N=int(input())

Board=[]
for i in range(N):
    Board.append(list(input()))

outside=[]
outside=Board[0]+[Board[i][-1] for i in range(1,N-1)]+Board[-1][::-1]+[Board[i][0] for i in range(N-2,0,-1)]

rotated_outside=[outside[-1]]+outside[:-1]
top=rotated_outside[:N]
right=rotated_outside[N:2*N-2]
bottom=rotated_outside[2*N-2:3*N-2][::-1]

left=rotated_outside[3*N-2:][::-1]



new_Board=[]
for i in range(N):
    if i==0:
        print(''.join(top))
        continue
    if i==N-1:
        print(''.join(bottom))
        continue
    
    new_row=[left[i-1]]+Board[i][1:N-1]+[right[i-1]]
    print(''.join(new_row))

def update_Board(row,col,power):
    
    Board[row][col]='.'
    broken_area=set()
    for d in range(0,power+1):
        for i in range(d+1):
            d_x=i
            d_y=d-i
            broken_area.add((row+d_y,col+d_x))
            broken_area.add((row+d_y,col-d_x))
            broken_area.add((row-d_y,col+d_x))
            broken_area.add((row-d_y,col-d_x))

    
    for area in broken_area:
        if (0<=area[0] and area[0]<R) and (0<=area[1] and area[1]<C):
            if Board[area[0]][area[1]]=='#':
                Board[area[0]][area[1]]='.'
                    

R,C=map(int,input().split())
Board=[]
for i in range(R):
    Board.append(list(input()))


for i in range(R):
    for j in range(C):
        if Board[i][j]!='.' and Board[i][j]!='#':
            update_Board(i,j,int(Board[i][j]))
for row in Board:
    print(''.join(row))

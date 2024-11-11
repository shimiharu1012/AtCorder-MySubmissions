# a1,b1,c1...
# a2,b2...

col=['a','b','c','d','e','f','g','h']
row=['1','2','3','4','5','6','7','8']
row.reverse()
Board=[]
for i in range(8):
    Board.append(list(input()))

def f():
    for i in range(len(row)):
        for j in range(len(col)):
            if Board[i][j]=='*':
                print(col[j]+row[i])
                return
            
f()
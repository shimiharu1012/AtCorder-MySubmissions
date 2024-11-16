S=input()

A=[len(s) for s in S.split('|') if s]
print(*A)
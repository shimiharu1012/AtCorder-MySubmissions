
N=int(input())
amount=0
Tj=0
for i in range(N):
    Ti,Vi=map(int,input().split())
    if amount>=(Ti-Tj):
        amount-=(Ti-Tj)
    else:
        amount=0

    amount+=Vi
    Tj=Ti

print(amount)
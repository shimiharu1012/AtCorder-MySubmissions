S=input()
order='ABCDEFGHIJKLMNOPQRSTUVWXYZ'

d=0
now=0
for i in range(26):
    # 全てのアルファベットに対して
    if i==0:
        for x in range(26):
            if S[x]=='A':
                now=x
    else:
        for x in range(26):
            if S[x]==order[i]:
                d+=abs(now-x)
                now=x


print(d)
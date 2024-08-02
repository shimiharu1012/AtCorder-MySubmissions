# A^A==BとなるAがあるかを調べる
# B<10^18
# A<18

B=int(input())
ans=-1
for A in range(1,18):
    if A**A==B:
        ans=A
        break

print(ans)
# 素朴な実装
# 全探索はN!通り

# ベースの高さは肩の高さAの総和
# その上で、頭が一番長いやつが最上にきてほしい

N=int(input())
P=[]
head=0
shoulder=0
for _ in range(N):
    A,B=map(int,input().split())
    # P.append([int(x) for x in input().split()])
    shoulder+=A
    head=B-A if B-A>head else head

print(shoulder+head)    
# -で分割された文字列について、最長の部分列を求め、そのうち最も長いものを
N=int(input())
S=input()


if S=='o'*N or S=='-'*N:
    print(-1)
else:
    subs=[len(s) for s  in S.split('-') if s]
    # print(max(subs,key=lambda x: len(x)))
    print(max(subs))



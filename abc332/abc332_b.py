
K,G,M=map(int,input().split())

grass=0
mag=0
for i in range(K):
    if grass==G:
        grass=0
    elif mag==0:
        mag=M
    else:
        water=min(mag,G-grass)
        grass+=water
        mag-=water


print(grass,mag)
# Sの連続部分列のうち、１種類の文字からなるもの
# 26種類のアルファベットについて、最長の連続数を求め、それを足せば良い
# 例えば、文字列Sの中でaが最も連続している部分がaaaaaだったら、
# aのみからなる連続部分列はa,aa,...aaaaaの5種類だとわかる
# b...zについても同様

# 各文字の最長連続数を調べるにはランレングス圧縮を使う
def run_length_encode(s):
    n=len(s)
    ans=[]
    l=0
    while l<n:
        r=l+1
        while r<n and s[l]==s[r]:
            r+=1
        ans.append((s[l],r-l))
        l=r
    
    return ans

N=int(input())
S=input()
rle=run_length_encode(S)
count=0
for i in range(26):
    _chr=chr(ord('a')+i)
    max=0
    
    for tuple in rle:
        if tuple[0]==_chr and tuple[1]>max:
            max=tuple[1]
    
    count+=max
    

print(count)
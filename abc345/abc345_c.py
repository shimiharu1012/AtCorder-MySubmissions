# 違うもじの箇所を２つ選ぶ方法の通り
# もし、全て同じ文字列の場合は、1を出力する
ord_a=ord('a')
def count_alphabet(s):
    '''文字列s内のアルファベットを数える'''
    alphabet_count={}
    
    for i in range(26):
        alphabet_count[chr(ord_a+i)]=s.count(chr(ord_a+i))
    
    return alphabet_count

S=input()
N=len(S)
alphabet_count=count_alphabet(S)

ans=0
for i in range(25):
    for j in range(i+1,26):
        ans+=alphabet_count[chr(ord_a+i)]*alphabet_count[chr(ord_a+j)]
    
# 一箇所でも同じ場所があれば１を足す

for i in range(26):
    if alphabet_count[chr(ord_a+i)]>1:
        ans+=1
        break
print(ans)


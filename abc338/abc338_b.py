S=input()

alphabet_count={}
ord_a=ord('a')
for i in range(26):
    alphabet_count[chr(ord_a+i)]=0


for s in S:
    alphabet_count[s]+=1

print(max(alphabet_count.items(),key=lambda x:x[1])[0])
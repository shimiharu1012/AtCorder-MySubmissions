S,T=input().split()

# Sをw文字ごとに区切る
# 飛び飛びにとっていったときに、Tに一致すれば良い

def f():

    for w in range(1,len(S)):
        split_list=[]
        s=S
        while len(s)>0:
            split_list.append(s[:w])
            s=s[w:]
        
        for c in range(1,w+1):
            t=""
            for sub in split_list:
                if len(sub)>=c:
                    t+=sub[c-1]

            if t==T:
                return True
    
    return False
            
print("Yes" if f() else "No")

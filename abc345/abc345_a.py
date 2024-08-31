S=input()
N=len(S)

def f():
       
    if S[0]!='<':
        print('No')
        return

    for i in range(1,N-1):
        if S[i]!='=':
            print('No')
            return

    if S[-1]!='>':
        print('No')
        return
    
    print('Yes')
    return


f()
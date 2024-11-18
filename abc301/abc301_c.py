# S,Tのアルファベットの個数を調べる
# BBBBaaaaa@
# BBBBddd@@@

def count_alphabet(s):
    '''文字列s内のアルファベットを数える'''

    alphabet_count={}
    ord_a=ord('a')
    for i in range(26):
        alphabet_count[chr(ord_a+i)]=s.count(chr(ord_a+i))
    
    return alphabet_count


atcard=list("atcorder")
S=input()
T=input()

S_count=count_alphabet(S)
T_count=count_alphabet(T)
S_at=0
T_at=0
for c in S:
    if c=='@':
        S_at+=1

for c in T:
    if c=='@':
        T_at+=1


def f(S_at,T_at):
    ord_a=ord('a')
    

    S_atcard_diff=0
    T_atcard_diff=0
    for i in range(26):
        if chr(ord_a+i) in atcard:
            if S_count[chr(ord_a+i)]>T_count[chr(ord_a+i)]:
                # S_atcard_diff[chr(ord_a+i)]=S_count[chr(ord_a+i)]-T_count[chr(ord_a+i)]
                S_atcard_diff+=S_count[chr(ord_a+i)]-T_count[chr(ord_a+i)]
            elif S_count[chr(ord_a+i)]<T_count[chr(ord_a+i)]:
                T_atcard_diff+=T_count[chr(ord_a+i)]-S_count[chr(ord_a+i)]
            else:
                pass
        elif S_count[chr(ord_a+i)]!=T_count[chr(ord_a+i)]:
            print("No")
            return

    if S_atcard_diff<=T_at and T_atcard_diff<=S_at:
        print("Yes")
    else:
        print("No")

    return    

f(S_at,T_at)
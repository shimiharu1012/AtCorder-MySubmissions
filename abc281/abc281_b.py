S=input()
N=len(S)
alphabet=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

if S[0] in alphabet and S[1:-1].isdecimal() and S[1]!='0' and S[-1] in alphabet:
    print("Yes")
else:
    print("No")
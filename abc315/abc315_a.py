S=input()
T=""
NG=['a','i','u','e','o']

for i in range(len(S)):
    if not S[i] in NG:
        T+=S[i]

print(T)
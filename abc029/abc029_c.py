N=int(input())
chr_list=['a','b','c']

def dfs(s):
    if len(s)==N:
        print(s)
        return
    
    for chr in ['a','b','c']:
        s+=chr
        dfs(s)
        s=s[:-1]

dfs('')



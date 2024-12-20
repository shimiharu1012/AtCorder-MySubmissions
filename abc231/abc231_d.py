class UnionFind:
    def __init__(self,n):
        self.n=n
        self.parent_size=[-1]*n
    
    def find(self,a):
        '''aの所属するグループのrootをfindする'''
        if self.parent_size[a]<0:
            return a
        self.parent_size[a]=self.find(self.parent_size[a])
        return self.parent_size[a]
    
    def union(self,a,b):
        '''a,bの所属するグループをunionする'''
        x,y=self.find(a),self.find(b)
        if x==y:
            return
        if abs(self.parent_size[x])<abs(self.parent_size[y]):
            x,y=y,x
        self.parent_size[x]+=self.parent_size[y]
        self.parent_size[y]=x
        return
    
    def same(self,a,b):
        '''同一グループかどうかを確認する'''
        return self.find(a)==self.find(b)

    def size(self,a):
        '''所属するグループのサイズを確認する'''
        return abs(self.parent_size[self.find(a)])
    
    def groups(self):
        '''グループ全体の確認'''
        result=[[] for _ in range(self.n)]
        for i in range(self.n):
            result[self.find(i)].append(i)
        
        return [r for r in result if r!=[]]
    
        

# 条件をグラフに落とし込む
# ３人と隣あう人がいる場合、その時点で１列じゃない＝NO
# 一周ぐるっと平路になる場合もNo
N,M=map(int,input().split())

UF=UnionFind(N+1)
count=[0]*(N+1)


for i in range(M):
    A,B=map(int,input().split())
    count[A]+=1
    count[B]+=1

    if count[A]>=3 or count[B]>=3:
        print('No')
        exit()
    
    # A,Bがすでに同じグループにいる場合
    # A,Bを隣合わせにすることで、閉路ができてしまう
    # したがって、条件を満たさない->Noを出力
    if UF.same(A,B):
        print('No')
        exit()
    else:
        # A,Bが隣り合っていることをUFに反映する
        UF.union(A,B)


print("Yes")    

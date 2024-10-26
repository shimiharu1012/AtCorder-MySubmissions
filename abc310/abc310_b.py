# 商品iに対して

# Pi=>Pj
# iの持つ機能を全て持つ
# 

N,M=map(int,input().split())
prods=[]
for i in range(N):
    In=[int(x) for x in input().split()]
    prod_i={"id":i,"price":In[0],"func_n":In[1],"funcs":set(In[2:])}
    prods.append(prod_i)


def compare():
    for i in range(N):
        for j in range(N):
            # 値段を比較する
            if prods[i]['price']<prods[j]['price']:
                continue
            
            # 機能を比較する
            if prods[i]['funcs']<prods[j]['funcs'] or \
            (prods[i]['funcs']==prods[j]['funcs'] and prods[i]["price"]>prods[j]["price"]):
                
                return True
            

    return False


print("Yes" if compare() else "No")
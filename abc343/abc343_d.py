# TxNだと間に合わない
# したがって、得点が増加した人についてのみ重複になるかを調べ
# なるなら-1、ならないならそのまま
# 誰が何点取っているかは必要


N,T=map(int,input().split())
diversity=N
scores_list=[0]*(N+1)
scores_dict={0:N}
for i in range(T):
    A,B=map(int,input().split())
    scores_dict[scores_list[A]]-=1
    if scores_dict[scores_list[A]]==0:
        scores_dict.pop(scores_list[A])
    
    scores_list[A]+=B
    if scores_list[A] in scores_dict:
        scores_dict[scores_list[A]]+=1
    else:
        scores_dict[scores_list[A]]=1

    print(len(scores_dict))



    
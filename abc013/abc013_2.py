# ディスプレイの番号は1桁(mod10)
# 

a=int(input())
b=int(input())

print(min((a-b)%10,(b-a)%10))
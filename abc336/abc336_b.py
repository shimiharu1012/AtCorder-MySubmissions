N=int(input())

# Nを2進数表記にしたとき、末尾に連続する0の個数

N_bin=bin(N)

for i in range(len(N_bin)):
    if N_bin[-(i+1)]=='0':
        pass
    else:
        break

print(i)
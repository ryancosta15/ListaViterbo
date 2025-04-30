n = int(input())
j = 1
k = 2 
nao = True
continua = True
for i in range (0,n -1):       
    if (i*j*k) == n:
        nao = False
        print("Este número satisfaz a propriedadde")
        print(f"{i} x {j} x {k} = {n}")
    j+=1
    k+=1
if nao:
    print("Este número não satisfaz a propriedade")

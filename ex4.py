n = int(input())
#primeiro número
x = 0
#segundo número
y = 1

print(x, end =  " ")
print(y, end = " ")

#n-1 pois já tiraram 2, ou seja, (n+1)-2 = n-1
for i in range(n-1):
    #soma dos dois últimos
    z = x + y
    print(z, end = " ")
    #anda a fila
    x = y
    y = z

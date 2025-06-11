def criar_matriz():
    matriz = []
    for i in range (2):
        row = []
        for j in range(2):
            a = float(input(f"elemento a{i}{j} "))
            row.append(a)
        matriz.append(row)
    return matriz
a = criar_matriz("A")
b = criar_matriz("B")
c = []
for i in range (2):
    row = []
    for j in range(2):
        e = a[i][j] + b[i][j]
        row.append(e)
    c.append(row)

print("-"*5)
print("MATRIZ")
for row in c:
    print(row)

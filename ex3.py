a = []
b = []
#criando a matriz A
ma = float(input("A m: "))
na = float(input("A n: "))
for i in range(ma):
    row = []
    for j in range(na):
        e = float(input(f"elemento A a{i}{j} "))
        row.append(e)
    a.append(row)
#criando a matriz B
mb = float(input("B m: "))
nb = float(input("B n: "))
for i in range(mb):
    row = []
    for j in range(nb):
        e = float(input(f"elemento B b{i}{j} "))
        row.append(e)
    b.append(row)
#C = A * B
if len(ma) == len(b) and len(na) == len(b[0]):
    c = []
    for i in range(ma):
        row = []
        for j in range(nb):
            e = 0
            for k in range(na):
                e += a[i][k] * b[k][j]
            row.append(e)
        c.append(row)
#print A, B e C
    print("-"*5)
    print("MATRIZ A")
    for row in a:
        print(row)
    print("-"*5)
    print("MATRIZ B")
    for row in b:
        print(row)
    print("-"*5)
    print("MATRIZ C")
    for row in c:
        print(row)
else:
    print("As matrizes não podem ser multiplicadas, verifique as dimensões.")
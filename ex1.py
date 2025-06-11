matriz = []
k = float(input("k: "))
for i in range (3):
    row = []
    for j in range (3):
        a = float(input(f"elemento a{i}{j}"))
        row.append(a if i != j else a * k)
    matriz.append(row)
for row in matriz:
    print(row)
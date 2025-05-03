import math
h1 = int(input())
m1 = int(input())
t1 = h1 * 60 + m1
h2 = int(input())
m2 = int(input())
t2 = h2 * 60 + m2
tarifa = 0
tempo = math.ceil((t2 - t1) / 60)

if tempo >= 1:
	tarifa += 8
elif tempo >= 2:
	tarifa += 6
elif tempo >= 3:
	tarifa += 3.5
#4 e 5 cobra por hora
elif tempo >= 4:
	tarifa += 3 * (min(tempo, 5) - 3)
elif tempo >= 6:
	tarifa += 2 * (tempo - 5)
else:
	print("Tempo inválido")

print(f"Tarifa: R$ {tarifa:.2f}")

investimento = float(input("Investimento Mensal: "))
taxa = float(input("Taxa de Juros:")) / 100 + 1
valor = 0
continuar = True
while continuar:
	for i in range(1, 13):
		valor *= taxa
		valor += 100
	print(f"Saldo: R${round(valor, 2)}")
	processar_proximo_ano = True if input("Deseja calcular o ano seguinte? (S/N) ").upper == "S" else False

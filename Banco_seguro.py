saldo = 1000.0

def ver_saldo():
	print(f"seu saldo é: {saldo}$")
	
def sacar():
	global saldo
	try:
		while True:
			valor = float(input("Digite o valor de saque: "))
			if valor > saldo or valor < 1:
				print("O valor não pode ser superior ao saldo ou menor que 1$")
			else:
				saldo -= valor
				print(f"você sacou: {valor}$ e ficou com {saldo}$ de saldo")
				break
	except ValueError:
				print("Use apenas números e pontos")

while True:
	print("1 - ver saldo")
	print("2 - sacar")
	print("3 - sair")
	
	while True:
		try:
			menu = int(input("Digite: "))
			if menu in (1, 2, 3):
				break
			else:
				print("Ação Inválida")
		except ValueError:
			print("Digite apenas números")
			
	if menu == 1:
		ver_saldo()
	elif menu == 2:
		sacar()
	elif menu == 3:
		print("PROGRAMA FINALIZADO ")
		break

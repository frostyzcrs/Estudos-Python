vaga_ocupada = []
faturamento = 0

while True:
	print("1 - entrar carro")
	print("2 - sair carro")
	print("3 - faturamento total")
	print("4 - sair")
	
	while True:
		menu = int(input("digite: "))
		if menu in (1,2,3,4):
			break
		else:
			print("número inválido")
			
			
	if menu == 1:
		hora_entrada = int(input("digite a hora de entrada: "))
		placa = input("digite a placa: ")
		carro = {"hora_entrada": hora_entrada, "placa": placa}
		vaga_ocupada.append(carro)
		
	elif menu == 2:
		carro_placa_sair = input("digite a placa do carro: ")
		encontrado = False
		for carro in vaga_ocupada:
			if carro['placa'] == carro_placa_sair:
				encontrado = True
				while True:
					carro_hora_sair = int(input("digite a hora que o carro está saindo: "))
					if carro_hora_sair > carro['hora_entrada']:
						 break
					else:
						print("o tempo de saída não pode ser menor que o de entrada")
				tempo = carro_hora_sair - carro['hora_entrada']
				conta = tempo * 10
				vaga_ocupada.remove(carro)
				faturamento += conta
				print(f"A conta será: {conta}$")
				break
		if encontrado == False:
				print("carro não existe")
				
	elif menu == 3:
				print(f"O faturamento total é: {faturamento}$")
				
	elif menu == 4:
				print("PROGRAMA FINALIZADO ")
				break

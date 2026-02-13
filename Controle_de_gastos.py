while True:
	print("1 - adicionar gasto")
	print("2 - ver total de gastos")
	print("3 - sair")

	while True:
		menu = int(input("digite: "))
		if menu <= 3 and menu > 0:
			break
		else:
			print("acao invalida")
			
	if menu == 1:
		item_nome = input("digite o nome do item: ")
		item_valor = float(input("digite o valor do item: "))
		with open("meus_gastos.txt", "a") as arquivo:
			arquivo.write(f"{item_nome}, {item_valor}\n")
			print("gasto salvo com sucesso")
	
	elif menu == 2:
		total = 0
		try:
				with open("meus_gastos.txt", "r") as arquivo:
					linhas = arquivo.readlines()
					if not linhas:
						print("o arquivo está vazio")
					else:
						print("seus gastos")
						for linha in linhas:
							nome, valor = linha.strip().split(",")
							print(f"item: {nome} | valor: {valor}")
							total += float(valor)
						print(f"total acumulado: {total:.2f}$")
		except FileNotFoundError:
								print("nenhum gasto registrado ainda")
			
	elif menu == 3:
		print("PROGRAMA FINALIZADO")
		break

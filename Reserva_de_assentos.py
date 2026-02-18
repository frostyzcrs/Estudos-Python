assentos_livres = list(range(1, 21))
assentos_vendidos = []
while True:
	if len(assentos_livres) == 0:
		print("todos os ingressos foram vendidos")
		break
		
	print("1 - mostrar assentos")
	print("2 -  comprar ingreso")
	print("3 - sair")
	
	while True:
		menu = int(input("digite: "))
		if menu in (1, 2, 3):
			break
		else:
			print("acao invalida")
	
	if menu == 1:
		print(f"número de acentos disponíveis: {assentos_livres}")
		
	elif menu == 2:
		ingreso = int(input("digite o número do assento: "))
		for assento in assentos_livres:
			if ingreso == assento:
			 	assentos_livres.remove(assento)
			 	assentos_vendidos.append(assento)
			
	else:
		break

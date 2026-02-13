filmes = []

while True:
	print("1 - adicionar filme")
	print("2 - listar filmes")
	print("3 - atualizar filme")
	print("4 - deletar filme")
	print("5 - somar dois filmes")
	print("6 - sair")
	
	while True:
		menu = int(input("digite: "))
		if menu > 0 and menu <= 6:
			break
		else:
			print("digite um número válido")
			
	if menu == 1:
		filme_id = len(filmes) + 1
		filme_nome = input("digite o nome do filme: ")
		filme_valor = float(input("digite o valor do filme: "))
		novo_filme = {"filme_id": filme_id, "filme_valor": filme_valor, "filme_nome": filme_nome}
		filmes.append(novo_filme)
		
	elif menu == 2:
		if len(filmes) < 1:
			print("Nao há filmes")
		else:
			for filme in filmes:
				print(f"ID: {filme['filme_id']} | Nome: {filme['filme_nome']} | Valor: {filme['filme_valor']}")
				
	elif menu == 3:
		id_alterar = int(input("Digite o ID do filme que deseja alterar: "))
		encontrado = False
		for filme in filmes:
			if filme['filme_id'] == id_alterar:
				encontrado = True
				novo_filme_nome = input("digite o novo nome do filme: ")
				novo_filme_valor = float(input("Digite o novo valor do filme: "))
				filme['filme_nome'] = novo_filme_nome
				filme['filme_valor'] = novo_filme_valor
				break
		if encontrado == False:
			print("ID não existe")
			
	elif menu == 4:
		id_deletar = int(input("Digite o ID do filme que deseja delatar: "))
		encontrado = False
		for filme in filmes:
			if filme['filme_id'] == id_deletar:
				encontrado = True
				filmes.remove(filme)
				print(f"O filme {filme['filme_nome']} foi deletado")
				break
		if encontrado == False:
			print("ID não existe")
			
	elif menu == 5:
		filme_1_id = int(input("Digite o ID do primeiro filme: "))
		filme_2_id = int(input("Digite o ID do segundo filme: "))
		f1_encontrado = False
		f2_encontrado = False
		for filme in filmes:
			if filme['filme_id'] == filme_1_id:
				soma1 = filme['filme_valor']
				nome1 = filme['filme_nome']
				f1_encontrado = True
		for filme in filmes:
			if filme['filme_id'] == filme_2_id:
				soma2 = filme['filme_valor']
				nome2 = filme['filme_nome']
				f2_encontrado = True
		if f1_encontrado == True and f2_encontrado == True:
			print(f"A soma dos filmes: {nome1} e {nome2} é: {soma1 + soma2}")
		if f1_encontrado == False and f2_encontrado == False:
			print("Um dos IDs não existe")
			
	elif menu == 6:
			print("PROGRAMA FINALIZADO")
			break

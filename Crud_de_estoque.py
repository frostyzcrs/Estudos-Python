produtos = []
produto_id = 0

while True:
	print("1 - adicionar produto")
	print("2 - listar produtos")
	print("3 - editar produto")
	print("4 - remover produto")
	print("5 - relatório de produtos")
	print("6 - Sair")
	
	while True:
		menu = int(input("digite"))
		if menu <= 6 and menu > 0:
			break
		else:
			print("digite um número válido")
			
	if menu == 1:
		produto_id += 1
		produto_nome = input("digite o nome do produto: ")
		while True:
			produto_quantidade =int(input("digite a quantidade do produto: "))
			if produto_quantidade > 0:
				break
			else:
				print("quantidade não pode ser 0")
		produto_minimo = int(input("digite a quantidade mínima do produto: "))
		novo_produto = {"id": produto_id, "nome": produto_nome, "quantidade": produto_quantidade, "minimo": produto_minimo}
		produtos.append(novo_produto)
		
	elif menu == 2:
		if len(produtos) <= 0:
			print("não há produtos")
		else:
			for produto in produtos:
				print(f"ID: {produto['id']} | Nome: {produto['nome']} | Quantidade: {produto['quantidade']} | Mínimo: {produto['minimo']}")
				
	elif menu == 3:
		id_alterar = int(input("digite o ID do produto que deseja alterar: "))
		encontrado = False
		for produto in produtos:
			if id_alterar == produto['id']:
				encontrado = True
				novo_produto_nome = input("digite o nome do produto: ")
				novo_produto_quantidade = int(input("digite a quantidade do produto: "))
				novo_produto_minimo = int(input("digite a quantidade mínima do produto: "))
				produto["nome"] = novo_produto_nome
				produto['quantidade'] = novo_produto_quantidade
				produto['minimo'] = novo_produto_minimo
				break
		if encontrado == False:
			print("ID não Existe ")
			
	elif menu == 4:
		id_excluir = int(input("digite o ID que deseja excluir: "))
		encontrado = False
		for produto in produtos:
			if id_excluir == produto['id']:
				encontrado = True
				produtos.remove(produto)
				break
		if encontrado == False:
			print("ID não existe")
			
	elif menu == 5:
			if len(produtos) <= 0:
				print("não há produtos")
			else:
				for produto in produtos:
					if produto['quantidade'] < produto['minimo']:
						print(f"⚠️ O produto: {produto['nome']} | ID: {produto['id']} Tem menos quantidade que o mínimo {produto['quantidade']}/{produto['minimo']}")
						
	elif menu == 6:
			print("programa finalizado")
			break

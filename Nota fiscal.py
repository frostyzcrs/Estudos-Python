#SOMA DE PRODUTOS 

produtos = []
produto_id = 0

while True:
	print("1- Adicionar Produto")
	print("2 - Somar Produtos")
	print("3 - Tirar Produto")
	print("4 - FECHAR")
	
	#garante uma escolha do menu
	while True:
		try:
			menu = int(input("digite: "))
			if menu in (1, 2, 3, 4):
				break
			else:
				print("⚠️ NÚMERO INVÁLIDO")
		except ValueError:
			print("⚠️ DIGITE APENAS NÚMEROS")
			
	#adiciona produto
	if menu == 1:
		print("•" * 32)
		print("digite (sair) no nome do produto para sair")
		try:
			while True:
				produto_nome = input("Nome do produto: ")
				if produto_nome == "sair":
					break
				produto_id += 1
				produto_valor = float(input("Valor do produto: "))
				while True:
					produto_quantidade = int(input("Quantidade: "))
					print("•" * 32)
					if produto_quantidade >= 1:
						break
					else:
						print("⚠️ QUANTIDADE INVÁLIDA")
				novo_produto = {"id": produto_id, "nome": produto_nome, "valor": produto_valor, "quantidade": produto_quantidade}
				produtos.append(novo_produto)
				print(f"{produto_quantidade} {produto_nome} de {produto_valor}R$ Adicionado ✔️")
		except ValueError:
						print("⚠️ ERRO DE DIGITAÇÃO")
						
	#faz a soma dos produtos					
	elif menu == 2:
						if len(produtos) <= 0:
							print("não há produtos")
						else:
							print("•" * 32)
							print("=== PRODUTOS ===")
							total = sum(produto['valor'] * produto['quantidade'] for produto in produtos)
							for produto in produtos:
								print(f"{produto['nome']} | R$ {produto['valor']} | x{produto['quantidade']}")
							print("=== TOTAL ===")
							print(f"{total: .2f}R$")
							print("•" * 32)
							
	#retira um produto							
	elif menu == 3:
		try:
			if len(produtos) <= 0:
				print("não há produtos")
			else:
				for produto in produtos:
					print(f"ID: {produto['id']} | {produto['nome']} | R$ {produto['valor']} | x{produto['quantidade']}")
				id_exlcluir = int(input("Digite o ID a excluir: "))
				encontrado = False
				for produto in produtos:
					if id_exlcluir == produto['id']:
						encontrado = True
						produtos.remove(produto)
						print(f"ID: {produto['id']} | {produto['nome']} | R$ {produto['valor']} | x{produto['quantidade']} | EXCLUIDO")
						break
				if encontrado == False:
						print("Produto não encontrado")
		except ValueError:
						print("⚠️ ERRO DE DIGITAÇÃO")
						
	elif menu == 4:
		print("PROGRAMA FINALIZADO")

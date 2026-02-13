pedido = {
    "id": 1,
    "cliente": "Daniel",
    "item": "Hambúrguer",
    "quantidade": 2,
    "status": "Pendente"
}

pedidos = []

while True:
	print("1 - Adicionar Pedido")
	print("2 - Listar Pedidos")
	print("3 - Atualizar Pedidos")
	print("4 - Alterar Status do Pedido")
	print("5 - Deletar Pedido")
	print("6 - Sair")
	menu = int(input("Escolha Uma Opção "))
	if menu == 1:
		cliente_nome = input(str("Digite Seu Nome: "))
		pedido_nome = input(str("Digite o Nome do Lanche: "))
		while True:
			pedido_quantidade = int(input("Digite a Quantidade: "))
			if pedido_quantidade >= 1:
				break
			else:
				print("Quantidade Invalida")
		status_atual = "pendente"
		id_valor = len(pedidos) + 1
		novo_pedido = {"id": id_valor, "cliente": cliente_nome, "item": pedido_nome, "quantidade": pedido_quantidade, "status": status_atual}
		pedidos.append(novo_pedido)
		
	elif menu == 2:
		if len(pedidos) == 0:
			print("Não há Pedidos Ainda")
		else:
			for pedido in pedidos:
				print(f"ID: {pedido['id']} | Cliente: {pedido['cliente']} | Item: {pedido['item']} | Quantidade: {pedido['quantidade']} | Status: {pedido['status']}")
				
	elif menu == 3:
		id_alterar = int(input("Digite o ID Que Deseja Alterar: "))
		encontrado = False
		for pedido in pedidos:
			if pedido['id'] == id_alterar:
				encontrado = True
				novo_pedido_nome = input(str("Digite o Nome Do Novo Lanche: "))
				novo_pedido_quantidade = int(input("Digite a Quantidade Nova: "))
				pedido['item'] = novo_pedido_nome
				pedido['quantidade'] = novo_pedido_quantidade
				break
		if encontrado == False:
			print("ID Não Existe")
			
	elif menu == 4:
		encontrado = False
		pedido_id_valor = int(input("Digite o ID do Pedido Para Atualizar: "))
		for pedido_id in pedidos:
			if pedido_id['id'] == pedido_id_valor:
				encontrado = True
				print("1 - Pendente")
				print("2 - Em Preparo")
				print("3 - Entregue")
				acao = int(input("Escolha o Status: "))
				if acao == 1:
					novo_status = "Pendente"
				elif acao == 2:
					novo_status = "Em Preparo"
				elif acao == 3:
					novo_status = "Entregue"
				pedido_id['status'] = novo_status
				print(f"O Status Atual do Pedido {pedido_id['item']} é {pedido_id['status']}")
		if encontrado == False:
			print("ID Não Existe!")
			
	elif menu == 5:
		pedido_id = int(input("Digite o ID do Pedido: "))
		encontrado = False
		for p in pedidos:
			if p['id'] == pedido_id:
				encontrado = True
				pedidos.remove(p)
				print(f"O pedido: {p['item']} De: {p['cliente']} Foi Removido")
				break
		if encontrado == False:
				print("ID Não Existe")
				
	elif menu == 6:
		print("Programa Finalizado")
		break				

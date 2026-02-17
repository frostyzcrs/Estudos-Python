pacientes = []

while True:
	print("1 - Adicionar paciente")
	print("2 - chamar proximo")
	print("3 - mostrar fila")
	print("4 - sair")
	
	while True:
		menu = int(input("digite: "))
		if menu >= 1 and menu <= 4:
			break
		else:
			print("número inválido")
			
	if menu == 1:
			paciente_nome = input(str("Digite o nome do paciente: "))
			print("prioridade")
			print("1 -  vermelho")
			print("2 - amarelo")
			print("3 -  verde")
			acao = int(input("digite: "))
			if acao == 1:
				paciente_prioridade = "vermelho"
			elif acao == 2:
				paciente_prioridade = "amarelo"
			else:
				paciente_prioridade = "verde"
				
			novo_paciente = {"nome": paciente_nome, "prioridade": paciente_prioridade}
			
			pacientes.append(novo_paciente)
			
	elif menu == 2:
			atendido = False
			for paciente in pacientes:
				if paciente['prioridade'] == "vermelho":
					print(f"o paciente {paciente['nome']} com prioridade {paciente['prioridade']} será atendido")
					pacientes.remove(paciente)
					atendido = True
					break
					
					
			if not atendido:
					for paciente in pacientes:
						if paciente['prioridade'] == "amarelo":
							print(f"o paciente{paciente['nome']} com prioridade {paciente['prioridade']} será atendido")
							pacientes.remove(paciente)
							atendido = True
							break
					
					
			if not atendido:
						for paciente in pacientes:
							if paciente['prioridade'] == "verde":
								print(f"o paciente {paciente['nome']} com prioridade {paciente['prioridade']} será atendido")
								pacientes.remove(paciente)
								atendido = True
								break
								
	elif menu == 3:
		if len(pacientes) == 0:
			print("não há pacientes")
		else:
			print("FILA")
			for paciente in pacientes:
				print(f"Paciente nome: {paciente['nome']} | Prioridade: {paciente['prioridade']}")
			
	else:
		break

alunos = []

while True:
	print("1 - Cadastrar aluno")
	print("2 - Lançar notas")
	print("3 - Ver medias")
	print("4 - Sair")
	
	while True:
		menu = int(input("Digite: "))
		if menu in (1, 2, 3, 4):
			break
		else:
			print("Ação Invalida")
			
	if menu == 1:
			aluno_nome = input("Digite o nome do aluno: ")
			novo_aluno = {"nome": aluno_nome, "notas": []}
			alunos.append(novo_aluno)
			
	elif menu == 2:
		if len(alunos) == 0:
			print("Não há alunos")
		else:
			for aluno in alunos:
				print(f"Aluno(a): {aluno['nome']}")
				nota_1 = float(input("Digite a primeira nota: "))
				nota_2 = float(input("Digite a segunda nota: "))
				nota_3 = float(input("Digite a terceira nota: "))
				aluno['notas'].append(nota_1)
				aluno['notas'].append(nota_2)
				aluno['notas'].append(nota_3)
			print("Notas lançadas")
				
	elif menu == 3:
		if len(alunos) == 0:
			print("Não há alunos")
		else:
			for aluno in alunos:
				media = sum(aluno['notas'])
				media = media / 3
				if media >= 7:
					situacao = "Aprovado"
				else:
					situacao = "Reprovado"
				print(f"Nome: {aluno['nome']} | {situacao}")
				
	elif menu == 4:
				print("PROGRAMA FINALIZADO ")
				break

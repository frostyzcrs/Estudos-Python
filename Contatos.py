import json

contatos = []

try:
	with open("agenda.json", "r") as f:
		contatos = json.load(f)
except FileNotFoundError:
	contatos = []

def adicionar_contato():
	contato_nome = input(str("digite o nome do contato: "))
	contato_telefone = int(input("digite o número do contato: "))
	novo_contato = {"nome": contato_nome, "telefone": contato_telefone}
	contatos.append(novo_contato)
	
	with open("agenda.json", "w") as f:
		json.dump(contatos, f, indent=4)
		print("contato salvo")
	
def listar_contatos():
	if len(contatos) <= 0:
		print("não ha contatos")
	else:
		for contato in contatos:
			print(f"Nome: {contato['nome']} | Telefone: {contato['telefone']}")
			
while True:
	print("1 - adicionar contato")
	print("2 - listar contatos")
	print("3 - sair")
	while True:
		menu = int(input("digite: "))
		if menu >= 1 and menu <= 3:
			break
		else:
			print("opção invalida")
	if menu == 1:
		adicionar_contato()
	elif menu == 2:
		listar_contatos()
	else:
		print("programa finalizado")
		break

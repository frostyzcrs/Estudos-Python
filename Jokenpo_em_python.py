import random

while True:
	rodadas = int(input("digite a quantidade de rodadas: "))
	if rodadas > 0:
		break
	else:
		print("digite um número superior a 0")
		
lista = ["pedra", "papel", "tesoura"]

jogador_vitorias = 0
ia_vitorias = 0

def jogar(rodadas):
	global jogador_vitorias, ia_vitorias
	print("digite")
	print("1-pedra | 2-papel | 3-tesoura")
	ia_escolha = random.choice(lista)
	jogador_escolha = int(input(""))
	if jogador_escolha == 1:
		acao = "pedra"
	elif jogador_escolha == 2:
		acao = "papel"
	else:
		acao = "tesoura"
		
	if ia_escolha == "pedra" and acao == "pedra":
		print("empate")
	elif ia_escolha == "pedra" and acao == "papel":
		print("Você Ganhou")
		jogador_vitorias += 1
	elif ia_escolha == "pedra" and acao == "tesoura":
		print("Você Perdeu")
		ia_vitorias += 1
		
	elif ia_escolha == "papel" and acao == "pedra":
			print("Você Perdeu")
			ia_vitorias += 1
	elif ia_escolha == "papel" and acao == "papel":
		print("empate")
	elif ia_escolha == "papel" and acao == "tesoura":
		print("Você Ganhou")
		jogador_vitorias += 1
		
	elif ia_escolha == "tesoura" and acao == "pedra":
		print("Você Ganhou")
		jogador_vitorias += 1
	elif ia_escolha == "tesoura" and acao == "papel":
		print("Você Perdeu")
		ia_vitorias += 1
	elif ia_escolha == "tesoura" and acao == "tesoura":
		print("empate")
		
	print(f"A IA escolheu: {ia_escolha} e Você Escolheu: {acao}")
	print("=" * 31)
		

while rodadas > 0:
	jogar(rodadas)
	rodadas -= 1

print("PLACAR")
print(f"Vitórias do jogador: {jogador_vitorias} | Vitórias da IA: {ia_vitorias}")

import random

palavras = ["python", "programacao", "desafio"]

palavra_sorteada = random.choice(palavras)

letras_acertadas = ["_"] * len(palavra_sorteada)

while True:
	try:
		if "_" not in letras_acertadas:
				print("você ganhou")
				break
		print(" ".join(letras_acertadas))
		palpite = input(str("digite uma letra: "))
		for i, letra in enumerate(palavra_sorteada):
			if palpite.lower() == letra:
				letras_acertadas[i] = palpite
	except ValueError:
				print("digite apenas letras")

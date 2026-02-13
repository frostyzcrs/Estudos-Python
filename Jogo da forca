import random

tentativas = 6

palavras = ["abacate", "cadeira", "teclado"]

palavra = random.choice(palavras)

letras_descobertas = ["_"] * len(palavra)
letras_erradas = []

while tentativas > 0:
	print(" ".join(letras_descobertas))
	if "_" not in letras_descobertas:
		print("Você Ganhou")
		break
	letra = input(str("digite uma letra: ")).lower()
	if letra in letras_erradas:
		print("Você já usou essa letra")
		continue
	if letra in palavra:
		for l in range(len(palavra)):
			if palavra[l] == letra:
				letras_descobertas[l] = letra
	else:
		letras_erradas.append(letra)
		print(f"Letras erradas: {letras_erradas}")
		tentativas -= 1
		print(f"Você tem {tentativas} tentativas restantes")
		
if tentativas == 0:
	print(f"Game Over a palavra era: {palavra}")

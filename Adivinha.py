import random

numero_secreto = random.randint(1, 100)
tentativas = 0

while True:
	try:
		palpite = int(input("digite: "))
		if palpite == numero_secreto:
			break
		elif palpite < numero_secreto:
			print("chute mais alto")
			tentativas += 1
		elif palpite > numero_secreto:
			print("chute mais baixo")
			tentativas += 1
	except ValueError:
		print("Digite apenas números")
		
print(f"Parabéns você acertou em {tentativas} tentativas")

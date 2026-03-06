nomes = ["Daniel", "Zacarias", "Lima"]

with open("meus_dados.txt", "w") as arquivo:
	for nome in nomes:
		arquivo.write(nome + "\n")
		
print("✔️ arquivo criado e nomes salvos")

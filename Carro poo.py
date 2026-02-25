class carro:
	def __init__(self, marca, modelo, combustivel):
		self.marca = marca
		self.modelo = modelo
		self.combustivel = combustivel
		
	def dirigir(self, km):
		gasto = km * 0.1
		if self.combustivel <= gasto:
			print("não há combustível")
		else:
			self.combustivel -= gasto
			print(f"o modelo {self.modelo} rodou {km} km restam {self.combustivel}")
			
	def abastecer(self, litros):
		self.combustivel += litros
		print(f"o {self.modelo} foi abastecido com {litros} litros. total {self.combustivel}")

meu_carro = carro("pegassi", "zentorno", 10)
outro_carro = carro("honda", "civic", 100)

meu_carro.abastecer(100)
meu_carro.dirigir(10)
outro_carro.dirigir(30)

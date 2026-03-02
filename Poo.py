class Veiculo:
	def __init__(self, marca, modelo):
		self.marca = marca
		self.modelo = modelo
	
	def buzinar(self):
		print("Bibibi")
		
class Moto(Veiculo):
	def empinar(self):
		print("Grau")
		
meu_carro = Veiculo("Honda", "Civic")
minha_moto = Moto("Kawasaki", "ninja")

meu_carro.buzinar()
minha_moto.empinar()

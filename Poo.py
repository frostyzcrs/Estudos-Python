class Veiculo:
	def __init__(self, marca, modelo):
		self.marca = marca
		self.modelo = modelo
	
	def buzinar(self):
		print("Bibibi")
		
class Moto(Veiculo):
	def __init__(self, marca, modelo, cilindrada):
		super().__init__(marca, modelo)
		self.cilindrada = cilindrada
			
	def empinar(self):
		print("Grau")
		
	def detalhes(self):
		print(self.marca, self.modelo, self.cilindrada)
		
meu_carro = Veiculo("Honda", "Civic")
minha_moto = Moto("Kawasaki", "ninja", "100")

meu_carro.buzinar()
minha_moto.empinar()
minha_moto.detalhes()

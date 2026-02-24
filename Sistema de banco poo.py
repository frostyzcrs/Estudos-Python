class ContaBancaria:
	def __init__(self, titular, saldo_inicial):
		self.titular = titular
		self.saldo = saldo_inicial
		
	def depoisitar(self, valor):
		self.saldo += valor
		print(f"Depósito de R${valor} realizado!")
		
	def ver_saldo(self):
		print(f"Saldo atual de {self.titular}: R${self.saldo:.2f}")
		
	def sacar(self, valor):
		if valor <= self.saldo:
			self.saldo -= valor
			print(f"saque de {valor} realizado!")
		else:
			print("saldo insuficiente")
		
minha_conta = ContaBancaria("seu nome", 1000.0)

minha_conta.ver_saldo()
minha_conta.depoisitar(200)
minha_conta.ver_saldo()
minha_conta.sacar(100)
minha_conta.ver_saldo()

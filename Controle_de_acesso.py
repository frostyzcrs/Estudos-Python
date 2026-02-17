usuario_correto = "teste@gmail.com"
senha_correta = 123
tentativas = 3

while tentativas > 0:
	usuario = input("digite o usuário: ")
	senha = int(input("digite a senha: "))
	if usuario == usuario_correto and senha == senha_correta:
		print("acesso permitido")
		break
	else:
		print("usuário ou senha incorretos")
		tentativas -= 1
		print(f"você tem: {tentativas} tentativas")
		
if tentativas == 0:
	print("acesso negado")

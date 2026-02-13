def validar_senha(senha):
	tem_maiuscula = False
	tem_minuscula = False
	tem_numero = False
	tamanho_ok = len(senha) >= 8
	for x in senha:
		if x.isupper():
			tem_maiuscula = True
		if x.islower():
			tem_minuscula = True
		if x.isdigit():
			tem_numero = True
			
	if not tem_maiuscula:
		print("a senha precisava ter pelo menos 1 letra maiúscula")
	if not tem_minuscula:
		print("a senha precisa ter pelo menos 1 letra minúscula")
	if not tem_numero:
		print("a senha precisa ter pelo menos um número")
	if not tamanho_ok:
		print("a senha precisa ter mais de 8 caracteres")
		
	if tem_maiuscula and tem_minuscula and tem_numero and tamanho_ok:
			return True
	else:
		return False
	
senha = input("digite a senha")

if validar_senha(senha):
	print("senha forte")
else:
	print("senha fraca")

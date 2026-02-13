print("calculadora")
print("=" * 31)
print("digite")
print ("1 somar, 2 dividir, 3 subtração, 4 multiplicação ")
number1 = int(input("digite o 1 numero"))
number2 = int(input("digite o segundo numero"))
menu = int(input("digite a acao"))
if menu == 1:
	resultado = number1 + number2
elif menu == 2:
	resultado = number1 / number2
elif menu == 3:
	resultado = number1 - number2
elif menu == 4:
	resultado = number1 * number2
print(resultado)

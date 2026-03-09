import tkinter as tk

janela = tk.Tk()
janela.title("calculadora")
janela.geometry("400x300")

texto = tk.Label(janela, text="calculadora")
texto.pack(pady = 20)

tk.Label(janela, text="número 1").pack()
num1=tk.Entry(janela)
num1.pack()

tk.Label(janela, text="número 2").pack()
num2=tk.Entry(janela)
num2.pack()

resultado = tk.Label(janela, text="Resultado: ")
resultado.pack(pady=10)

def somar():
	try:
		valor1 = float(num1.get())
		valor2 = float(num2.get())
		result = valor1 + valor2
		resultado.config(text=f"Resultado: {result}", fg="black")
	except ValueError:
		resultado.config(text="digite apenas numeros", fg="red")
		
def subtrair():
	try:
		valor1 = float(num1.get())
		valor2 = float(num2.get())
		result = valor1 - valor2
		resultado.config(text=f"Resultado: {result}", fg="black")
	except ValueError:
		resultado.config(text="digite apenas numeros", fg="red")
		
def multiplicar():
	try:
		valor1 = float(num1.get())
		valor2 = float(num2.get())
		result = valor1 * valor2
		resultado.config(text=f"Resultado: {result}", fg="black")
	except ValueError:
		resultado.config(text="digite apenas numeros", fg="red")
	
frame_botoes = tk.Frame(janela)
frame_botoes.pack(pady=10)

botao_soma = tk.Button(frame_botoes, text="somar", command=somar)
botao_soma.pack(side="left", padx=5)

botao_subtrair = tk.Button(frame_botoes, text="subtrair", command=subtrair)
botao_subtrair.pack(side="left", padx=5)

botao_multiplicar = tk.Button(frame_botoes, text="multiplicar", command=multiplicar)
botao_multiplicar.pack(side="left", padx=5)

janela.mainloop()

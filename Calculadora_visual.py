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
		soma = valor1 + valor2
		resultado.config(text=f"Resultado: {soma}")
	except ValueError:
		resultado.config(text="digite apenas numeros", fg="red")
	
botao = tk.Button(janela, text="somar", command=somar)
botao.pack(pady=10)

janela.mainloop()

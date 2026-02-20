tarefas = []

while True:
  print("lista de tarefas")
  print("1 - ver tarefas | 2 - nova tarefa | 3 - marcar como pronto | 4 - sair")

  while True:
    menu = int(input("digite: "))
    if menu <= 4 and menu >= 1:
      break
    else:
      print("digite um numero valido")

  if menu == 1:
    if len(tarefas) < 1:
      print("nao ha tarefas")
    else:
      for tarefa in tarefas:
        print(f"Titulo: {tarefa['titulo']}, Descrição: {tarefa['desc']}")

  elif menu == 2:
    novo_titulo = input("digite o titulo: ")
    nova_desc = input("digite a descricao: ")
    nova_tarefa = ({"titulo": novo_titulo, "desc": nova_desc})
    tarefas.append(nova_tarefa)

  elif menu == 3:
    encontrado = False
    tarefa_pronta = input("digite o titulo da tarefa")
    for tarefa in tarefas:
      if tarefa['titulo'] == tarefa_pronta:
        encontrado = True
        tarefas.remove(tarefa)
        print(f"a tarefa: {tarefa['titulo']} foi concluida")
        break
    if encontrado == False:
      print("tarefa nao encontrada")

  elif menu == 4:
    print("programa finalizado")
    break
      

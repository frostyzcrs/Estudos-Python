import random, time

ia_msgs = ["valeu", "oi", "tudo bem", "salve", "tendi", "serio", "aham ta", "bom", "ok",]
contatos = []

while True:
  print("1 registrar contato")
  print("2 conversar")
  print("3 sair")
  print("=" * 31)

  while True:
    menu = int(input("digite: "))
    if menu > 0 and menu < 4:
      break
    else:
      print("digite um numero valido")

  if menu == 1:
    contato_id = len(contatos) + 1
    contato_nome = input("digite o nome do contato: ")
    contato_numero = int(input("digite o numero do contato: "))
    novo_contato = {"id": contato_id, "nome": contato_nome, "numero": contato_numero}
    contatos.append(novo_contato)

  elif menu == 2:
    conversar_com = int(input("digite o numero do contato: "))
    encontrado = False
    for contato in contatos:
      if conversar_com == contato['numero']:
        encontrado = True
        print("digite xxx para sair")
        while True:
          ia_msg = random.choice(ia_msgs)
          u_msg = input("digite: ")
          if u_msg == "xxx":
            break
          else:
            time.sleep(1)
            print(f"{contato['nome']}: {ia_msg}")
    if encontrado == False:
      print("contato nao encontrado")

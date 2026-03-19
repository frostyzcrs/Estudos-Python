transacoes = []

def cadastrar():
    try:
        transacao_nome = input("Digite o nome da transação: ")
        transacao_valor = int(input("Digite o valor da transação: "))
        transacao_categoria = input("Digite a categoria da transação: ")
        nova_transacao = {"nome": transacao_nome, "valor": transacao_valor, "categoria": transacao_categoria}
        transacoes.append(nova_transacao)
    except ValueError:
        print("Erro de digitação")

def ver_saldo():
    if len(transacoes) == 0:
        print("Nao ha transações")
    else:
        saldo = sum(transacao['valor'] for transacao in transacoes)
        for transacao in transacoes:
            if transacao['valor'] > 0:
                print(f"{transacao['nome']} | {transacao['valor']}$ | {transacao['categoria']}")
            elif transacao['valor'] <= 0:
                print(f"{transacao['nome']} | {transacao['valor']}$ | {transacao['categoria']} [!]")
        print(f"Seu saldo: {saldo}$")
        if saldo <= 0:
            print("Cuidado você està no vermelho")

def relatorio_por_categoria():
    if len(transacoes) == 0:
        print("Nao ha transações")
    else:
        try:
            categoria_alvo = input("Digite o nome da categoria: ").lower()
            encontrado = False
            total_gategoria = 0 #valor total da categoria
            print(f"Transações de: {categoria_alvo}")
            for transacao in transacoes:
                if transacao['categoria'].lower() == categoria_alvo.lower():
                    encontrado = True
                    total_gategoria = sum(transacao['valor'] for transacao in transacoes if transacao['categoria'].lower() == categoria_alvo)
                    print(f"{transacao['nome']} | {transacao['valor']} | {transacao['categoria']}")
            if encontrado == True:
                if total_gategoria <= 0:
                    print(f"O total de gastos da categoria: {categoria_alvo} é: {total_gategoria}$")
                else:
                    print("Nao há gastos nesta categoria")
            if encontrado == False:
                print("Categoria não encontrada")
        except ValueError:
            print("Erro de digitação")

def remover_transacao():
    if not transacoes:
        print("Não há transações")
    else:
        try:
            encontrado = False
            print("Todas as transações")
            for i, transacao in enumerate(transacoes):
                print(f"{i} - {transacao['nome']} - {transacao['valor']}")

            transacao_remover = int(input("Digite o numero para remover: "))
            for i, transacao in enumerate(transacoes):
                if transacao_remover == i:
                    encontrado = True
                    transacoes.pop(i)
                    print(f"{transacao['nome']} de {transacao['valor']}$ Removida")
                    break
            if encontrado == False:
                print("Transação nao encontrada")
        except ValueError:
            print("Erro de digitação")

while True:
    print("1 - Cadastrar")
    print("2 - Ver saldo")
    print("3 - Relatorio por categoria")
    print("4 - Remover transação")

    while True:
        try:
            menu = int(input("Digite: "))
            if menu in(1, 2, 3, 4):
                break
            else:
                print("Ação invalida")
        except ValueError:
            print("Erro de digitacão")

    if menu == 1:
        cadastrar()
    elif menu == 2:
        ver_saldo()
    elif menu == 3:
        relatorio_por_categoria()
    elif menu == 4:
        remover_transacao()

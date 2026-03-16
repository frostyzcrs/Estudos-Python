transacoes = []

def cadastrar():
    try:
        transacao_nome = input("digite o nome da transacao: ")
        transacao_valor = int(input("digite o valor da transacao: "))
        transacao_categoria = input("digite a categoria da transacao: ")
        nova_transacao = {"nome": transacao_nome, "valor": transacao_valor, "categoria": transacao_categoria}
        transacoes.append(nova_transacao)
    except ValueError:
        print("erro de digitacao")

def ver_saldo():
    if len(transacoes) == 0:
        print("nao ha transacoes")
    else:
        saldo = sum(transacao['valor'] for transacao in transacoes)
        for transacao in transacoes:
            if transacao['valor'] > 0:
                print(f"{transacao['nome']} | {transacao['valor']}$ | {transacao['categoria']}")
            elif transacao['valor'] <= 0:
                print(f"{transacao['nome']} | {transacao['valor']}$ | {transacao['categoria']} [!]")
        print(f"Seu saldo: {saldo}$")
        if saldo <= 0:
            print("cuidado voce esta no vermelho")

while True:
    print("1 - cadastrar")
    print("2 - ver saldo")

    while True:
        try:
            menu = int(input("digite: "))
            if menu in(1, 2):
                break
            else:
                print("acao invalida")
        except ValueError:
            print("erro de digitacao")

    if menu == 1:
        cadastrar()
    elif menu == 2:
        ver_saldo()

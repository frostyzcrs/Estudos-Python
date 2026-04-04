class Aluno:
    def __init__(self, nome, nota1, nota2, nota3):
        self.nome = nome
        self.nota1 = nota1
        self.nota2 = nota2
        self.nota3 = nota3

    def calcular_media(self):
        media = (self.nota1 + self.nota2 + self.nota3) / 3
        return media

def adicionar_aluno():
    nome = input('digite o nome do aluno: ')
    nota1 = int(input('digite a nota 1 do aluno: '))
    nota2 = int(input('digite a nota 2 do aluno: '))
    nota3 = int(input('digite a nota 3 do aluno: '))
    aluno = Aluno(nome, nota1, nota2, nota3)
    alunos.append(aluno)

alunos = []

while True:
    print('1-adicionar aluno')
    print('2-calcular medias')
    print('3-sair')

    while True:

        menu = int(input('Digite: '))
        if menu in (1, 2, 3):
            break
        else:
            print('opcao invalida')

    if menu == 1:
        adicionar_aluno()
    elif menu == 2:
        if not alunos:
            print('não há alunos')
        else:
            for aluno in alunos:
                media = aluno.calcular_media()
                print(f'Aluno: {aluno.nome} | Média: {media:.2f}')

    elif menu == 3:
        print("Saindo...")
        break

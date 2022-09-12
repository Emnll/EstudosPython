# O programa tem como objetivo receber a nota dos alunos e então dizer a menor nota
print("-----"*5)
print("Escola Santa Paciência")
print("-----"*5)
alunos = int(input("Quantos alunos a turma tem? "))
lisnota= []
lisnome = []
lisgeral = []
asso = {}
i = 0
notas = []
while(i < alunos):
    nome = input("Nome do aluno: ")
    nota = input("Nota de " + nome + ": ")
    print("------"*5)
    i = i + 1
    lisnota.append(nota)
    lisnome.append(nome)
    tup = (nota, nome)
    lisgeral.append(tup)
lisnota.sort()
print("A menor nota foi:" + lisnota[0])
print(lisnome)
print(lisgeral)


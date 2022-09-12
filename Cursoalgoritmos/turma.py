nome = []
n1 = []
n2 = []
m = []
c = 0
sm = 0
mt = 0
for i in range(4):
    print("ALUNO " + str(i))
    nome.append(input("Nome: "))
    n1.append(input("Primeira nota: "))
    n2.append(input("Segunda nota: "))
    m.append((int(n1[i])+ int(n2[i]))/2)
    sm = sm + m[i]
mt = sm/4

print("Listagem de alunos:")    
print("-------"*5)
for i in range(4):
    print(nome[i], m[i])
    if(m[i]>mt):
        tot = tot + 1
print("Ao todo temos " + str(tot) + "alunos que estão acima da média da turma que foi " + str(mt))
#Utilizando a definição de funções o programa analisa se um número é par ou ímpar
def pop(v):
    if(v%2 == 0):
      print("O número " + str(v) + " é par")
    else:
        print("O número " + str(v) + " é ímpar")  

n = int(input("Digite um número: "))
pop(n)
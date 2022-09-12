#Este pequeno programa recebe a quantidade de números desejadas e então conta quantos números negativos foram colocados
n = int(input("Quantos números você quer contar? "))
i = 0
lista = []
cont = 0

while(i < n):
    num = int(input("Digite um número: "))
    lista.append(num)
    i = i + 1
    if(num < 0):
        cont = cont + 1
    else:
        continue

print(lista)
print("A quantidade de números negativos é:" + cont)

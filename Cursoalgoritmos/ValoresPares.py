
val = []
totpar = 0
for i in range(7):
    val.append(input("Digite o " + str(i) + "o. valor: "))
    if(int(val[i]) % 2 == 0):
        totpar = totpar + 1
    else: 
        continue
print("O total de pares foi: " + str(totpar))
for i in range(7):
    if(int(val[i])%2==0):
        print("Número par na posição " + str(i+1))
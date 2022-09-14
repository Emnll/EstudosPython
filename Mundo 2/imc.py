alt = input("Qual sua altura em metros? ")
peso = input("Qual o seu peso? ")
imc =  float(peso)/(float(alt)*float(alt))
print("Seu imc é de: " + str(imc))
if imc < 18.5:
    print("Você está abaixo do peso!")
elif imc <= 24.9:
    print("Seu peso está ideal!")
elif imc <= 30:
    print("Você está com sobrepeso!")
elif imc <= 40:
    print("Você está com obesidade!")
elif imc > 40:
    print("Você está com obesidade mórbida!")
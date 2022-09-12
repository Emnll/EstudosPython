#Calcula se o ano é bissexto ou não
#Calculates if its a leap year
a = int(input('Digite um ano: '))
if a/4 == 0 and a / 100 != 0 or a / 400 == 0:
    print(a,' é um ano bissexto!')
else: 
    print(a, ' não é um ano bissexto!')

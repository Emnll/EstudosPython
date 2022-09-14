ano = int(input("Em que ano o atleta nasceu? "))
idade = 2022 - ano
if idade <= 9:
    print("A categoria do atleta é MIRIM!")
elif idade <= 14:
    print("A categoria do atleta é INFANTIL!")
elif idade <= 19: 
    print("A categoria do atleta é JUNIOR!")
elif idade == 20:
    print("A categoria do atleta é SêNIOR")
elif idade > 20:
    print("A categoria do atleta é MASTER!")
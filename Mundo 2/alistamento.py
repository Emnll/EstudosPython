ano = int(input("Em que ano você nasceu? "))
idade = 2022 - ano
if idade < 18:
    print("Você terá de se alistar no ano de: "+ str((18-idade)+2022) )
elif idade == 18:
    print("Você tem que se alistar!!")
elif idade > 18:
    alis = input("Você se alistou? (S/N) ")
    if alis == "S":
        print("Muito bem!")
    else:
        print("Você está {} ano(s) atrasado para o alistamento!".format(str(idade-18)))

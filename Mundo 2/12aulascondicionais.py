nome = (str(input("Qual o seu nome? ")))
if nome == "Emanuelle":
    print("Que nome bonito!")
elif nome == "Pedro" or "João" or "Maria" or "Julia":
    print("Seu nome é bem comum!")
elif nome in "Ana Cláudia Jéssica Juliana":
    print("Adorei seu nome!")
else:
    print("Que nome legal!")
print("Tenha um bom dia {}! ".format(nome))

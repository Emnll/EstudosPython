tipo = input("Me dê um valor e te direis que tipo é:")
print("O tipo primitivo desse valor é", type(tipo))
print("Só tem espaços?" , tipo.isspace())
print("É um número?" , tipo.isnumeric())
print("É alfabético?",tipo.isalpha())
print("É alfanumérico?",tipo.isalnum())
print("Está em maiúsculas?",tipo.isupper())
print('Está em minúsculas?',tipo.islower())
print("Está capitalizada?",tipo.istitle())
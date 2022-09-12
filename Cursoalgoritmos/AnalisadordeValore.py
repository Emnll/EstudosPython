#O programa recebe um total de 5 informações e então avalia qual foi o nome e peso daquele que teve o maior peso
mai = 0
def topo():
    print("----------"*3)
    print("D E T E C T O R   DE  P E S A D O")
    print("Maior peso até agora: "+ str(mai) + "Kg")
    print("----------"*3)

topo()
for i in range (5):
    N = input("Digite o nome: ")
    P = input("Digite o peso de " + N + ": ")
    if (int(P) > int(mai)):
        mai = P
        pesado = N
    else:
        topo()    
topo()
print("A pessoa mais pesada foi " + pesado + ", com " + str(mai) + " quilos")   

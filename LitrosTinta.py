# Calculo de área para se calcular quantos litros de tinta serão usados
l = int(input("Qual a largura da parede em metros? "))
a = int(input("Qual a altura da parede em metros? "))
area = a * l 
tinta = (area//2) + 1
print('Se a parede tem {} de altura e {} de largura, logo sua área é de {} e terão que ser utilizados ao menos {} litros de tinta'.format(a,l,area,tinta))
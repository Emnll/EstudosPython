#Assume o input como uma distância em metros e converte em outras medidas de distância
#Assumes the input number as meters and converts it into other distance types
m = int(input('Digite um número: '))
km = m / 1000
hm = m / 100
dam = m / 10
dm = m * 10
c = m * 100
mm = m * 1000
print('Se você tivesse caminhado {} metros, seria o mesmo que caminhar {} centímetros ou {} milimetros'.format(m,c,mm))
print('{}km = {}hm = {}dam = {}m = {}dm = {}c = {}mm'.format(km,hm,dam,m,dm,c,mm))


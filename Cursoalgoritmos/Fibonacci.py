# O programa escreve a sequência de fibonacci até 15 números
f = 0
i = 1
n = 0
c = 0
while(c<15):
    print(n)
    c = c + 1
    n = i + f
    f = i
    i = n
    

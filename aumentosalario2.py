#Calcula o aumento do salário baseando no atual salário do usuário
#Calculates a raise in salary based on the current wage of the user
s = float(input('Digite o valor do seu salário: '))
if s > 1250.0:
    print('Parabéns agora o valor do seu salário é de: ', s * 1.1)
else: 
    print('Parabéns agora o valor do seu salário é de: ', s * 1.15)
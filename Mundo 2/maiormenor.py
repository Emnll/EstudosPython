num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))
if num1 > num2:
    print("O número {} é maior que {}".format(num1,num2))
elif num2 > num1:
    print("O número {} é maior que {}".format(num2,num1))
elif num1 == num2:
    print("O número {} é igual a {}".format(num1, num2))
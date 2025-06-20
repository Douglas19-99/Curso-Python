num1 = input('Insira o primeiro número: ')
num2 = input('Insira o segundo número: ')


if num1.isdigit() and num2.isdigit():

    if num1 == num2:
        print('Os dois números inseridos são iguais.')

    elif num1 > num2:
        print('O primeiro número é maior que segundo.')

    elif num2 > num1:
        print('O segundo número é maior que o primeiro.')

else:
    print('Valores inválidos. tente novamente.')






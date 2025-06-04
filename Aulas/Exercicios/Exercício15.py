entrada1 = input('Qual seu peso atual? ')
entrada2 = input('Qual sua altura em mentros? ')

try:
    peso = float(entrada1)
    peso2 = float(entrada2)
    imc = peso / (peso2 * peso2)

    if imc >= 0 and imc < 18.5:
        print(f'Seu imc é', {imc}, 'você está abaixo do peso.'  )
    elif imc >= 18.5 and imc <= 24.9:
        print(f'Seu imc é', {imc}, 'seu peso está normal.'  )
    elif imc >= 25.0 and imc <= 29.9:
        print(f'Seu imc é', {imc}, 'você está com sobrepeso.'  )
    elif imc >= 30.0 and imc <= 34.9:
        print(f'Seu imc é', {imc}, 'você está com obesidade grau I.'  )
    elif imc >= 35.0 and imc <= 39.9:
        print(f'Seu imc é', {imc}, 'você está com obesidade grau II.'  )
    else:
        print('Obesidade Grau III')

except ValueError:
    print('Valor inválido. Tente novamente.')
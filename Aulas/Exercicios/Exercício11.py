'''
Escreva um programa que pede a idade do usuário e
diz se ele pode tirar a carteira de motorista (precisa ter 18 anos ou mais).
'''
idade = input('Digite sua idade: ')

if idade.isdigit():
    num = int(idade)

    if num >= 18:
        print('Você pode tirar a carteira de motorista.')

    else:
        print('Você não pode tirar a carteira de mostorista.')

else:
    print('Valor inválido. Tente novamente.')

'''
Peça um número inteiro e diga se ele é par ou ímpar.
'''

entrada = input('Digite um número inteiro: ')

try:
    num = int(entrada)
    if num % 2 == 0:
        print('O número é par.')

    else:
        print('O número é impar.')

except ValueError:
    print('Entrada inválida. Tente novamente.')

'''
Crie uma variável nome e verifique se ela está vazia.
Se estiver, exiba "Nome não informado".
'''
#if nome.strip() == "" verifica se a string está vazia depois de limpar os espaços.
#nome.strip() remove espaços em branco no início e no fim da string.

nome = input("Digite seu nome: ")
        
if nome.strip() == "": 
    print("Nome não informado.")
else:
    print(f"Olá, {nome}!")

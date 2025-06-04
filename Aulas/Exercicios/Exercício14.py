print('Menu de opções simples:')
print('Escolha uma das opções abaixo')
print('1. Ver saldo')
print('2. Fazer Depósito')
print('3. Sair')
print('-' * 20) # Imprime uma linha para separar


try:
    escolha_str = input('Digite o número da sua opção: ')
    escolha = int(escolha_str)

    if escolha == 1:
        print('Seu saldo atual é de R$1.000,00')

    elif escolha == 2:
        print('Por favor, insira o valor a ser depósitado: ')

    elif escolha == 3:
        print('Obrigado por utilizar nossos serviços! Até logo.')
    else:
        print('Opção inválida. Por favor, escolha um número entre 1 e 3.')

except ValueError:
    print('Entradas inválida. Por favor, digite um número inteiro correspondente à opção.')
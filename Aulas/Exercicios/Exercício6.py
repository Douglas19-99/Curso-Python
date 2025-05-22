'''
Peça os seguintes dados ao usuário:
Nome completo
Idade
E-mail

Exiba:

Nome em maiúsculas

Primeiro nome

Quantos caracteres o nome tem (sem espaços)

Se o e-mail contém "@" e "." (validação básica)
Caso algum campo esteja vazio:

Mostre: "Todos os campos são obrigatórios!"
''' 
e_mail = input('Seu email: ')
nome = input('Por favor, escreva seu nome completo: ')
idade = input('Sua idade: ')
sem_espaços = nome.replace(" ", "")

if nome:
    print(f'O seu nome completo em maiuscúlo é: {nome.upper()}')
    print(f'O seu primeiro nome é: {(nome.strip().split()[0])}')
    print(f'Seu nome completo tem {len(sem_espaços)} letras.')
 

while True:
    e_mail = input('Digite seu e-mail: ')
    if '@' in e_mail and '.' in e_mail and e_mail:
        print(f'E-mail válido.')
        break

    else:
        print('E-mail inválido.')


else:
    print('Todos os campos são obrigatórios')
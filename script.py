opcao = ''

while opcao != 'sair':
    print('1 - olá')
    print('2 - tchau')
    print('Digite "sair" para encerrar')

    opcao = input('Escolha: ')

    if opcao == '1':
        print('Olá')
    elif opcao == '2':
        print('tchau')


while True:
    senha = input('Digite a senha:')

    if senha == '1234':
        print('Acesso permitido')
        break

soma = 0
contador = 0

while contador < 10:
    soma += int(input('Digite um numero: '))
    contador += 1

print('A media é: ',soma / contador)


numero1 = int(input('Digite um numero: '))
numero2 = int(input('Digite outro numero: '))
numero3 = int(input('Digite outro numero: '))
numero4 = int(input('Digite outro numero: '))
numero5 = int(input('Digite outro numero: '))
numero6 = int(input('Digite outro numero: '))
numero7 = int(input('Digite outro numero: '))
numero8 = int(input('Digite outro numero: '))
numero9 = int(input('Digite outro numero: '))
numero10 = int(input('Digite outro numero: '))

media = (numero1 + numero2 + numero3 + numero4 + numero5 + numero6 + numero7 + numero8 + numero9 + numero10) / 10
print('sua media é: ',media,)
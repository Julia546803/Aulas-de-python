numero1 = int(input('Digite um numero:'))
numero2 = int(input('Digite outro numero:'))
soma = numero1 + numero2
print('A soma é:',soma,)

numero3 = float(input('Digite o primeiro numero:'))
numero4 = float(input('Digite o segundo numero:'))
numero5 = float(input('Digite o terceiro numero:'))
resultado = ((numero3 + numero4 + numero5) / 3)
print('A média aritmétrica é:',resultado)

b = float(input('Digite o valor da sua base:'))
a = float(input('Digite o valor da sua altura:'))
area = b * a
print('A area do retângulo é:',area,)

valor_em_metros = float(input('Digite o valor em metros:'))
valor_em_centimetros = valor_em_metros * 100
print('O resultado da conversão é',valor_em_centimetros,'cm')

numero6 = int(input('Digite um numero:'))
antecessor = numero6 - 1
sucessor = numero6 + 1
print('numero:',numero6,)
print('antecessor:',antecessor,)
print('sucessor',sucessor,)

numero7 = int(input('Digite um numero:'))
dobro = numero7 * 2
print('dobro:',dobro)
triplo = numero7 * 3
print('triplo:',triplo)
raiz_quadrada = numero7 ** 0.5
print('raiz quadrada:',raiz_quadrada)

idade = int(input('Digite sua idade:'))
dias = idade * 365
print('sua idade em dias é:',dias)

numero8 = int(input('digite um numero:'))
numero9 = int(input('Digite outro numero:'))
soma = numero8 + numero9
print('Soma =',soma,)
subtracao = numero8 - numero9
print('Subtracao =',subtracao)
multiplicacao = numero8 * numero9
print('Multiplicacao =',multiplicacao)
divisao = numero8 / numero9
print('Divisao =',divisao)

produto = float(input('Digite o valor do produto:'))
desconto = produto * 0.10
preco_final = produto - desconto
print('O produto com 10% de desconto custa: R$',preco_final)

celsius = float(input('Digite um temperatura em celsius:'))
fahrenheit = (celsius * 9/5) + 32
print('O valor da temperatura em fahrenheit é de:',fahrenheit,'°F')

idade = int(input('Digite sua idade:'))
resultado = idade >= 18
print('Posso tirar a carteira de motorista:',resultado,)

numero10 = float(input('Digite um numero:'))
resultado = numero10 >= 10 and 20 >= numero10
print('Seu numero está e entre 10 e 20:',resultado,)

numero11 = float(input('Digite o primeiro numero:'))
verificacao = numero11 > 0
print('seu numero é positivo:',verificacao)

numero12 = int(input('Digite um numero'))
resultado = numero12 % 3 == 0 and numero12 % 5 == 0
print('Seu numero é multiplo de 3 e 5 ao mesmo tempo:',resultado,)

nota1 = float(input('Digite sua primeira nota:'))
nota2 = float(input('Digite sua segunda nota:'))
media = (nota1 + nota2) / 2
resultado = media >= 6
print('Você conseguiu passar de ano:',resultado,)

idade = int(input('Digite sua idade:'))
resposta = input('concluiu o ensino medio? responda com (sim/não):')
concluiu_ensino_medio = resposta == 'sim'
conclusao = idade >= 18 and resposta == 'sim'
print('Você pode se matricular nessa faculdade:',conclusao,)

cartao = input('Possui cartão de crédito? (sim/não): ')
ticket = input('Possui ticket? (sim/não): ')
cartao = cartao == 'sim'
ticket = ticket == 'sim'
resultado = cartao or ticket
print('Pode estacionar no estacionamento:',resultado)

conta_bloqueada = input('Sua conta está bloqueada? (sim/não): ')
conta_bloqueada = conta_bloqueada == 'sim'
resultado = not conta_bloqueada
print('Conta ativa?',resultado)

salario = float(input('Qual o seu salario:'))
nome_limpo = input('Seu nome é limpo? (sim ou nao)')
nome_limpo = nome_limpo == 'sim'
resultado = salario >= 2000 and nome_limpo
print('Pode pegar empréstimo',resultado)

idade = int(input('Digite sua idade:'))
tem_autorização = input('Você tem autorização do seu responsavel?')
tem_autorização = tem_autorização == 'sim'
resultado = idade >= 16 or idade >=12 and tem_autorização
print('Você pode entrar nesse filme:',resultado,)
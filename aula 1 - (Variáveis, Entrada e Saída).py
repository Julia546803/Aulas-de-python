nome = input('Digite seu nome: ')
print('Olá,', nome, 'seja bem-vindo(a)!')

idade = input('Digite sua idade: ')
print('Você tem',idade,'anos')

cidade = input('Digite a sua cidade:')
print('Você mora na cidade de',cidade,)

print('Digite dois numeros para saber sua somatória')
numero1 = float(input('digite um numero:'))
numero2 = float(input('digite outro numero:'))
soma = numero1 + numero2
print('A soma é:',soma,)

print('Digite dois numeros para saber o resultado de sua multiplicação')
numero3 = float(input('digite um numero:'))
numero4 = float(input('digite outro numero:'))
multiplicação = numero3 * numero4
print('A multiplicação é:',multiplicação,)

print('Digite um número cujo o dobro você deseja saber')
numero5 = float(input('digite um numero:'))
dobro = numero5 * 2
print('O dobro do',numero5,'é:',dobro,)

print('Digite um número cujo 0 triplo você deseja saber')
numero6 = float(input('digite um numero:'))
triplo = numero6 * 3
print('O triplo do',numero6,'é:',triplo,)

print('Digite um número para saber o seu quadrado')
numero7 = float(input('digite um numero:'))
quadrado = numero7 ** 2
print('O quadrado do',numero7,'é:',quadrado,)

print('Digite a largura e a altura de um retângulo de sua escolha')
L = float(input('digite a largura:'))
A = float(input('digite a altura:'))
área = L * A
print('A área do retângulo é:',área,)

print('Informe o valor do lado do quadrado para que a área seja calculada')
Q = float(input('digite o valor:'))
área2 = Q * Q
print('A área do quadrado é:',área2,)

numeral = input('digite um numero qualquer:')
print('O numero digitado foi:',numeral,)

nome = input('digite seu nome:')
idade = input('digite sua idade:')
print('Seu nome é',nome,'e você tem',idade,'anos')

print('Escolha dois numeros para saber o resultado de sua subtração')
numero8 = float(input('digite um numero:'))
numero9 = float(input('digite outro numero:'))
subtração = numero8 - numero9
print('O resultado da subtração é:',subtração,)

print('Escolha dois numeros para saber o resultado de sua divisão')
numero10 = float(input('digite um numero:'))
numero11 = float(input('digite outro numero:'))
divisao = numero10 / numero11
print('O resultado da divisão é:',divisao,)

print('Digite o valor do seu salário em reais')
numero10 = float(input('salário: R$'))
dobro = numero10 * 2
print('O dobro do seu salário é:',dobro,)

print('Digite um numero que queira saber sua metade')
numero11 = float(input('digite um numero:'))
metade = numero11 / 2
print('A metade de',numero11,'é:',metade,)

print('Digite três numeros que queira saber a sua respectiva somatória')
somatória1 = float(input('digite o primeiro numero:'))
somatória2 = float(input('digite o segundo numero:'))
somatória3 = float(input('digite o terceiro numero:'))
somatória = somatória1 + somatória2 + somatória3
print('A somatoria dos numeros',somatória1,'+',somatória2,'+',somatória3,'é igual:',somatória,)

print('Digite o preço de um produto de sua escolha para saber o seu respectivo valor com 10% de desconto')
produto = float(input('Digite o preço do produto: R$'))
desconto = produto * 10 / 100
preço_final = produto - desconto
print('O produto de sua escolha com 10% de desconto fica R$',preço_final,)

print('Informe a sua idade para que possa descobrir o ano de seu nascimento')
idade = int(input('Digite sua idade:'))
ano_nascimento = 2026 - idade
print('Você nasceu no ano de',ano_nascimento,)

nome = input('Digite seu nome:')
idade = input('Digite sua idade:')
cidade = input('Digite sua cidade:')
print('Olá',nome,',você tem',idade,'anos e mora na cidade de',cidade,)
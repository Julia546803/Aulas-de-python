usuario = input('Digite o nome do usuário:')
senha = input('Digite a senha:')
usuario_correto = 'admin'
senha_correto = 'python123'
if usuario == usuario_correto  and senha == senha_correto:
    print('Logado com sucesso')
else:
    print('Usuário ou senha incorreto')


temperatura = float(input('Digite o valor da temperatura em celsius:'))
if temperatura <= 14:
    print('Frio')
elif temperatura >= 15 and temperatura <= 24:
    print('Agradável')
else:
    print('Quente')


idade = int(input('Digite sua idade:'))
if idade <= 15:
    print('Não vota')
elif idade >= 16 and idade <= 17:
    print('Voto opcional')
elif idade >= 18 and idade <= 69:
    print('Voto obrigatório')
else:
    print('Voto opcional')


numero = int(input('Digite um numero de 1 a 7, para saber qual dia da semana ele equivale:'))
if numero == 1:
    print('Domingo')
elif numero == 2:
    print('Segunda')
elif numero == 3:
    print('Terça')
elif numero == 4:
    print('Quarta')
elif numero == 5:
    print('Quinta')
elif numero == 6:
    print('Sexta')
elif numero == 7:
    print('Sabado')
else:
    print('numero invalido')


peso = float(input('Digite o seu peso:'))
altura = float(input('Digite sua altura:'))
IMC = peso / (altura * altura)
if IMC >= 0 and IMC < 18.5:
    print('Abaixo do peso')
elif IMC >= 18.5 and IMC <= 24.9:
    print('Peso normal')
elif IMC >= 25 and IMC <= 29.9:
    print('Sobrepeso')
else:
    print('Obesidade')


numero = int(input('Digite um numero:'))
if numero % 3 == 0:
    print('O',numero,'é um múltiplo de 3')
else:
    print('O', numero,'não é um múltiplo de 3')


nota = float(input('Digite sua nota do 2°bimestre:'))
if nota >= 9 and nota <= 10:
    print('Sua nota é A')
elif nota >= 7 and nota <= 8:
    print('Sua nota é B')
elif nota >= 5 and nota <= 0:
    print('Sua nota é C')
else:
    print('Sua nota é D')


lado1 = float(input('Digite o valor do primeiro lado:'))
lado2 = float(input('Digite o valor do segundo lado:'))
lado3 = float(input('Digite o valor do terceiro lado:'))
if lado1 == lado2 and lado2== lado3:
    print('É um triângulo equilátero')
elif lado1 == lado2 or lado2 == lado3 or lado3 == lado1:
    print('É um triângulo isósceles')
else:
    print('É um triângulo escaleno')


numero = int(input('Digite um numero:'))
if numero >= 10 and numero <= 50:
    print('O número está entre 10 e 50.')
else:
    print('O número não está entre 10 e 50.')


produto = int(input('Digite o valor do produto:'))
if produto >= 1000:
    resultado = produto * 0.10
    resultado_final = produto - resultado
    print('você tem direito a um desconto de 10%, o valor final do seu produto é de R$',resultado_final)
elif produto >= 500:
    resultado = produto * 0.05
    resultado_final = produto - resultado
    print('Você tem direito a um desconto de 5%, o valor final do seu produto é de R$',resultado_final,)
else:
    print('Seu produto não possui desconto')


ano = int(input('Digite um ano para saber se é bissexto:'))
if ano % 4 == 0:
    print('O ano de',ano,'é bissexto')
else:
    print('O ano de',ano,'não é bissexto')


idade = int(input('Digite a sua idade:'))
if idade >= 0 and idade <= 12:
    print('Criança')
elif idade >= 13 and idade <= 17:
    print('Adolescente')
elif idade >= 18 and idade <= 59:
    print('Adulto')
else:
    print('Idoso')


numero1 = int(input('Digite um numero: '))
numero2 = int(input('Digite outro numero: '))
conta = input('escolha o calculo matemático que deseja efetuar:')
if conta == '+':
    resultado = numero1 + numero2
    print('O resultado do seu cálculo é:',resultado,)
elif conta == '-':
    resultado = numero1 - numero2
    print('O resultado do seu cálculo é:',resultado,)
elif conta == '*':
    resultado = numero1 * numero2
    print('O resultado do seu cálculo é:', resultado, )
elif conta == '/':
    if numero2 != 0:
        resultado = numero1 / numero2
        print('O resultado do seu cálculo é:', resultado, )
    else:
        print('Operação inválida!!, pois não é permitido divisão por 0')


print('Para acessar essa conta você deve inserir um código de quatro digitos')
senha = int(input('Digite a senha de acesso:'))
if senha == 1234:
    print('Senha validada com sucesso')
else:
    print('Senha invalida')


nota = float(input('Digite sua primeira nota: '))
nota1 = float(input('Digite sua segunda nota: '))
nota2 = float(input('Digite sua terceira nota: '))
nota3 = float(input('Digite sua terceira nota: '))
media = (nota + nota1 + nota2 + nota3) / 4
if media >= 7:
    print('Parabéns você foi aprovado!')
elif media >= 5 and media < 7:
    print('Você precisa fazer a prova de recuperação')
else:
    print('Você está reprovado')


numero1 = int(input('Digite um numero: '))
numero2 = int(input('Digite um numero: '))
numero3 = int(input('Digite um numero: '))
if numero1 > numero2 and numero1 > numero3:
    print('O maior numero é o',numero1)
elif numero2 > numero1 and numero2 > numero3:
    print('O maior numero é o',numero2)
else:
    print('O maior numero é o',numero3)


numero1 = int(input('Digite um numero:'))
numero2 = int(input('Digite outro numero:'))
if numero1 > numero2:
    print('O numero',numero1,'é maior que o numero',numero2,)
elif numero2 > numero1:
    print('O numero',numero2,'é maior que o numero',numero1,)
else:
    print('Os numero são iguais')


numero = int(input('Digite um numero: '))
if numero > 0:
    print('Seu numero é positivo (+)')
elif numero < 0:
    print('Seu numero é negativo (-)')
else:
    print('Seu numero é igual a zero')


idade = int(input('Digite sua idade:'))
if idade >= 18:
    print('Parabéns você é maior de idade')
else:
    print('Você é menor de idade, se retire')


numero = int(input('Digite um numero: '))
if numero % 2 == 0:
    print('par!')
else:
    print('impar')

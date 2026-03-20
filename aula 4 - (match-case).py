produto = float(input('Digite o valor do produto: '))

preco_final = produto * 0.90 if produto >= 100 else produto

print("Preço final:", preco_final)

numero = int(input('Digite um numero do setor que deseja saber: '))
match numero:
    case 1 | 2:
        print('Alimentos')
    case 3 | 4:
        print('Limpeza')
    case 5 | 6:
        print('Higiene')
    case _:
        print('Código inválido')

numero = int(input('Digite um numero 1 a 12 para saber o trimestre que esse mês pertence: '))
match numero:
    case 1 | 2 | 3:
        print('1° Trimestre')
    case 4 | 5 | 6:
        print('2° Trimestre')
    case 7 | 8 | 9:
        print('3° Trimestre')
    case 10 | 11 | 12:
        print('4° Trimestre')
    case _:
        print('Mês inválido')

nota = int(input('Digite sua nota: '))
resultado = (
    "Aprovado" if nota >= 7
    else "Recuperação" if nota >= 5
    else "Reprovado"
)
print(resultado)

numero1 = float(input('Digite um numero: '))
numero2 = float(input('Digite um numero: '))
operador = input('Digite o seu operador matemático: ')
match operador:
    case '+':
        print(numero1 + numero2)
    case '-':
        print(numero1 - numero2)
    case '*':
        print(numero1 * numero2)
    case '/':
        print(numero1 / numero2)
    case _:
        print('Operação inválida')

idade = int(input('Digite sua idade: '))
resultado = ('Você é maior de idade') if idade >= 18 else ('Você é menor de idade')
print(resultado)

numero = int(input('Digite um numero: '))
resultado = ('Par') if numero % 2 == 0 else ('Impar')
print(resultado)

turno = input('Digite o seu turno (m/t/n:) ').lower()
match turno:
    case 'm':
        print("Bom dia")
    case 't':
        print("Boa tarde")
    case 'n':
        print("Boa noite")
    case _:
        print("Turno inválido")

letra = input('Digite uma letra: ').lower()
match letra:
    case 'a'| 'e' | 'i' | 'o' | 'u':
        print('Essa letra é uma vogal')
    case _:
        print('Essa letra é uma consoante')

dias = int(input('Digite um numero para saber seu respectivo dia da semana:'))
match dias:
    case 1:
        print('domingo')
    case 2:
        print('Segunda')
    case 3:
        print('Terça')
    case 4:
        print('Quarta')
    case 5:
        print('quinta')
    case 6:
        print('Sexta')
    case 7:
        print('Sabádo')
    case _:
        print('Dia inválido')
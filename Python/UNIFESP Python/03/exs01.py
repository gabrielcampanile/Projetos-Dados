# 1 - Peça ao usuário suas notas das 3 unidades de uma disciplina e calcule sua média.
disciplina = input('Subject: ')
tamanho = 2
notas = []
media_final = 0

for i in range(0, tamanho):
    nota = float(input(f'Nota {i+1}: '))
    notas.append(nota)
    media_final += notas[i]

media_final /= tamanho

print(f'Sua média final em {disciplina} é {media_final:.2f}')

# 2 - Solicite ao usuário um inteiro positivo n e imprima a soma dos números pares entre 0 e n.
n = int(input('Digite um número inteiro: '))
for i in range(0, n+1, 2):
    print(i)

# 3 - Solicite ao usuário um inteiro positivo n e calcule o fatorial de n.
n = int(input("Digite um número inteiro: "))
fat = 1

for i in range(1, n+1):
    fat = fat * i

print(fat)

'''4 - Analise os números entre -25 e 50. Se o número for múltiplo de 2, imprima UNI.
 Se for múltiplo de 3, imprima FESP. Caso seja múltiplo de 2 e de 3 ao mesmo tempo, imprima UNI e FESP.'''

for i in range(-25, 50):
    if (i % 2 == 0 and i % 3 == 0):
        print(i, 'UNIFESP')
    elif (i % 2 == 0):
        print(i, 'UNI')
    elif (i % 3 == 0):
        print(i, 'FESP')

# Leia um inteiro e informe se ele é ou não múltiplo de 6.
n = int(input('n: '))
if n % 6 == 0:
    print(n, 'é múltiplo de 6')

# Leia duas idades de pessoas e se for maior de 18 anos, exibir uma mensagem dizendo: você é maior de idade.
for i in range(0,2):
    idade = int(input('Idade: '))
    if idade >= 18:
        print('Você é maior de idade.')

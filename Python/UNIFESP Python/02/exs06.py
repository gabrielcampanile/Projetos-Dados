# Leia um número e teste se ele é positivo, negativo ou nulo.

n = int(input('n: '))
if n > 0:
    print('Positivo')
elif n == 0:
    print('Nulo')
else:
    print('Negativo')

#múltiplas estruturas de decisão
from random import randint

numero = randint(0,100)
if numero % 6 == 0:
    print("O número", numero, "é múltiplo de 6!")
else:
    if numero % 2 == 0:
        print("O número", numero, "é múltiplo de 2, mas não de 3!")
    elif numero % 3 == 0:
        print("O número", numero, "é múltiplo de 3, mas não de 2!")
    else:
        print("O número", numero, "não é multiplo de 2 nem de 3, muito menos de 6!")
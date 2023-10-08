# 1 - Leia dois números inteiros e teste se o primeiro é menor do que o segundo.
from random import randint
a = int(input('Primeiro número: '))
b = int(input('Segundo número: '))
print(a < b)

# 2 - Sorteie dois números e teste se ambos são iguais.

a = randint(0, 10)
b = randint(0, 10)

print('A:', a)
print('B:', b)
if a > b:
    print('A é maior q B')
elif a == b:
    print('A é igual a B')
else:
    print('B é maior q A')

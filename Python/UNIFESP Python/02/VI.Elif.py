'''
if condicao_principal:
    # bloco se a condição principal for satisfeita
    expressao
    ...
elif condicao_alternativa_1:
    # bloco se a condição principal não for satisfeita mas a condição alternativa 1 for
    expressao
    ...
elif condicao_alternativa_2:
    # bloco se nem a condição principal nem a condição alternativa 1 forem satisfeitas, mas a condição alternativa 2 for
    expressao
    ...
...
else:
    # bloco se nem a condição principal nem as condições alternativas forem satisfeitas
    expressao
    ...
'''

a = 200
b = 33
if b > a:
  print("b é maior que a")
elif a == b:
  print("a e b são iguais")
else:
  print("a é maior que b")


from random import randint

numero = randint(1,6)
chute = int(input("Chute um número entre 1 e 6: "))
if chute == numero:
    print("Parabéns, você acertou!")
elif chute < numero:
    print("Seu chute foi menor que o número sorteado!")
else:
    print("Seu chute foi maior que o número sorteado!")
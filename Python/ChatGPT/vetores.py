#Criando um vetor:
vetor_vazio = []
vetor_com_valores = [1, 2, 3, 4, 5]

#Acessando elementos do vetor:
primeiro_elemento = vetor_com_valores[0]  # Acessa o primeiro elemento (valor 1)
terceiro_elemento = vetor_com_valores[2]  # Acessa o terceiro elemento (valor 3)

#Alterando elementos do vetor:
vetor_com_valores[1] = 10  # Altera o segundo elemento para 10

#Adicionando elementos ao vetor:
vetor_vazio.append(6)  # Adiciona o valor 6 ao final do vetor

#Removendo elementos do vetor:
vetor_com_valores.pop(2)  # Remove o terceiro elemento (valor 3)
vetor_com_valores.remove(4)  # Remove o elemento com valor 4

#Operações matemáticas com vetores:
vetor1 = [1, 2, 3]
vetor2 = [4, 5, 6]

soma = [x + y for x, y in zip(vetor1, vetor2)]  # Soma elemento a elemento: [5, 7, 9]

#Tamanho do vetor:
tamanho_vetor = len(vetor1)  # Retorna 3

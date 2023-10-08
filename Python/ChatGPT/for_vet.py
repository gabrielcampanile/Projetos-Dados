tamanho = 5  # Tamanho do vetor que você deseja criar
vetor = []   # Inicializando um vetor vazio

for _ in range(tamanho):
    valor = int(input("Digite um valor: "))  # Solicita um valor ao usuário
    vetor.append(valor)  # Adiciona o valor ao vetor

print("Vetor preenchido:", vetor)

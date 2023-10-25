import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Importando a base de vendas
base = pd.read_excel("Investimento x Venda.xlsx")

# Tipo do dado
type(base)

# Visualizando o DataFrame
base.head()

coluna = base["Investimento em marketing"]

# Tipo do dado
type(coluna)

# Visualizando a Series
coluna

# Pegando apenas os valores
coluna.values

# Pegando apenas os índices
coluna.index

# Pegando o valor de um índice específico
coluna[0]




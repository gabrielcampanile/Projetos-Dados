# Este projeto tem por objetivo desenvolver um algoritmo de Machine Learning para prever o valor do preço médio de casas em Boston.

import numpy as np
import pandas as pd

df = pd.read_csv('housing.csv', sep=',', encoding='iso-8859-1')

df.head()

**Atributos previsores**

> RM: é o número médio de cômodos entre os imóveis no bairro.

> LSTAT: é a porcentagem de propriet´rios no bairro considerados de "classe baixa" (proletariados)

> PTRATIO: é a razão entre estudantes e professores nas escolas de ensino fundamental e médio no bairro.

**Variável alvo**

> MEDV: valor médio das casas.

df.shape

independente = df.iloc[:, 0:3].values
independente

independente.shape

dependente = df.iloc[:, 3].values

dependente.shape

#TREINAMENTO 
from sklearn.model_selection import train_test_split
x_treino, x_teste, y_treino, y_teste = train_test_split(independente, dependente, test_size = 0.3, random_state = 0)

x_treino.shape, x_teste.shape

from sklearn.neural_network import MLPRegressor

redes = MLPRegressor(hidden_layer_sizes=(100,100), activation='relu', verbose=True,
                     max_iter=3000, solver='lbfgs', random_state=12)

redes.fit(x_treino, y_treino)

redes.n_layers_

redes.score(x_treino, y_treino)

#TESTE

redes.score(x_teste, y_teste)

previsoes_teste = redes.predict(x_teste)

#MÉTRICAS

from sklearn.metrics import mean_absolute_error, mean_squared_error

# Erro médio absoluto
mean_absolute_error(y_teste, previsoes_teste)

# Raix do erro quadrático médio (RMSE)
np.sqrt(mean_squared_error(y_teste, previsoes_teste))

# Erro médio absoluto percentual (MAPE)
np.mean(np.abs((y_teste - previsoes_teste) / y_teste)) * 100


import pandas as pd

#Leitura do dataset
df_diabetes = pd.read_csv("diabetes_prediction_dataset.csv")
display(df_diabetes)

#Exportação dos dados para excel
df_diabetes.to_excel('Dataset_diabetes.xlsx')

#Transformando valores de texto em números
df_diabetes = df_diabetes.replace('Female', 0)
df_diabetes = df_diabetes.replace('Male', 1)
df_diabetes = df_diabetes.replace('Other', 2)
print("0 - Female \n1 - Male\n")
display(df_diabetes)

#Observando valores de texto na coluna de histórico
#de fumar para se fazer a transformação
display(df_diabetes['smoking_history'].unique())
df_diabetes = df_diabetes.replace('never', 0)
df_diabetes = df_diabetes.replace('No Info', 1)
df_diabetes = df_diabetes.replace('current', 2)
df_diabetes = df_diabetes.replace('former', 3)
df_diabetes = df_diabetes.replace('ever', 4)
df_diabetes = df_diabetes.replace('not current', 5)
display(df_diabetes['smoking_history'])

#Exportação dos dados tratados para excel
df_diabetes.to_excel('Dataset_tratado_diabetes.xlsx')

#Separação do termos independentes para o cálculo
independente = df_diabetes.iloc[:, :8].values
independente

#Separação do termos objetivos para comparação
dependente = df_diabetes.iloc[:, 8].values
dependente

#Importando função para separação de treino e teste
from sklearn.model_selection import train_test_split
x_treino, x_teste, y_treino, y_teste = train_test_split(independente, dependente, test_size = 0.3, random_state = 0)

#Importando função de regressão
from sklearn.ensemble import RandomForestRegressor

random = RandomForestRegressor(n_estimators = 50, criterion ='squared_error', max_depth=10, random_state = 5)
random.fit(x_treino, y_treino)

#Observando a porcentagem de "acerto" no treino
random.score(x_treino, y_treino)

#Observando a porcentagem de "acerto" no teste
random.score(x_teste, y_teste)

from xgboost import XGBRegressor
xgboost = XGBRegressor(n_estimators = 50, max_depth = 4, leaning_rate = 0.05, objective ="reg:squarederror")
xgboost.fit(x_treino, y_treino)

xgboost.score(x_treino, y_treino)

xgboost.score(x_teste, y_teste)

#Importando função para padronização
from sklearn.preprocessing import StandardScaler

#Padronizando o x treino
x_scaler = StandardScaler()
x_treino_scaler = x_scaler.fit_transform(x_treino)

#Padronizando o y treino
y_scaler = StandardScaler()
y_treino_scaler = y_scaler.fit_transform(y_treino.reshape(-1, 1))

#Padronizando o x teste
x_scaler = StandardScaler()
x_teste_scaler = x_scaler.fit_transform(x_teste)

#Padronizando o y teste
y_scaler = StandardScaler()
y_teste_scaler = y_scaler.fit_transform(y_teste.reshape(-1, 1))

#Fazendo nova regressão
from xgboost import XGBRegressor
xgboost = XGBRegressor(n_estimators = 50, max_depth = 4, leaning_rate = 0.5, objective ="reg:squarederror")
xgboost.fit(x_treino_scaler, y_treino_scaler.ravel())

xgboost.score(x_treino_scaler, y_treino_scaler)

xgboost.score(x_teste_scaler, y_teste_scaler)
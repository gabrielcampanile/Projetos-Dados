# Responder a pergunta:
## "Vamos investir 75k em marketing, qual deve ser o estoque enviado pra loja?"

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

## IMPORTANDO A BASE DE VENDAS

# Importando a base de vendas
base = pd.read_excel("Investimento x Venda.xlsx")

# Exibindo as 5 primeiras linhas
base.head()

# Visualizando de forma gráfica essas informações
plt.scatter(base["Investimento em marketing"],base["Venda Qtd"])
plt.show()

## Traçando uma reta passando por esses pontos

plt.scatter(base["Investimento em marketing"],base["Venda Qtd"])
x0 = base["Investimento em marketing"][0]
y0 = base["Venda Qtd"][0]
x1 = base["Investimento em marketing"][6]
y1 = base["Venda Qtd"][6]
plt.plot([x0,x1],[y0,y1],"r")
plt.show()

## Usando a equação da reta para determinar a venda
### y = ax + b

def EncontraY(x_reta,y_reta,x):
    a = (y_reta[1] - y_reta[0])/(x_reta[1] - x_reta[0])
    b = y_reta[1] - a*x_reta[1]
    y = a*x + b
    return y

EncontraY([x0,x1],[y0,y1],75)

plt.scatter(base["Investimento em marketing"],base["Venda Qtd"])
plt.scatter(75,EncontraY([x0,x1],[y0,y1],75),color="k")
x0 = base["Investimento em marketing"][0]
y0 = base["Venda Qtd"][0]
x1 = base["Investimento em marketing"][6]
y1 = base["Venda Qtd"][6]
plt.plot([x0,x1],[y0,y1],"r")
plt.show()

## Descobrindo a venda usando Machine Learning

from sklearn import linear_model

reg = linear_model.LinearRegression()

reg.fit(base["Investimento em marketing"].values.reshape(-1, 1),base["Venda Qtd"])

reg.coef_

reg.intercept_

plt.scatter(base["Investimento em marketing"],base["Venda Qtd"])
x = np.array(base["Investimento em marketing"])
y = reg.intercept_ + x*reg.coef_
plt.plot(x,y,"r")
plt.show()

reg.predict([[75]])

plt.scatter(base["Investimento em marketing"],base["Venda Qtd"])
plt.scatter(75,reg.predict([[75]])[0],color="k")
x = np.array(base["Investimento em marketing"])
y = reg.intercept_ + x*reg.coef_
plt.plot(x,y,"r")
plt.show()


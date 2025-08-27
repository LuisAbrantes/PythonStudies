import pandas as pd
import io
from sklearn.linear_model import LinearRegression

dados_pizzas_csv = """diametro_cm,preco_reais
20,25
25,32
30,40
35,48
40,55
50,70
"""
dfPizzas = pd.read_csv(io.StringIO(dados_pizzas_csv))

print("Preparing data")
x = dfPizzas[["diametro_cm"]]
y = dfPizzas[["preco_reais"]]

print("Training model")
model = LinearRegression()
model.fit(x,y)
print("Model trained succesfully!")

print("Predicting data")
newPizza = [[45]]

pizzaPredict = model.predict(newPizza)

print(f"O preço da pizza previsto pelo modelo é de R$ {pizzaPredict[0][0]:.2f} mil.")
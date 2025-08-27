import pandas as pd
import io
from sklearn.linear_model import LinearRegression

# Os dados simulando um arquivo CSV
dados_salarios_csv = """anos_experiencia,salario_anual_mil
1.1,39
2.0,46
3.2,63
4.0,68
5.1,75
6.0,88
7.5,95
9.0,110
10.5,122
"""

dfSalaries = pd.read_csv(io.StringIO(dados_salarios_csv))

print("Preparing data")
X = dfSalaries[["anos_experiencia"]]
y = dfSalaries[["salario_anual_mil"]]
print("Data divided in X (anos_experiencia) and y (salario_anual_mil)")


print("Traingin model")
model = LinearRegression()
model.fit(X,y)
print("Model trained succefully!")


print("Predicting data")
newEmployee = [[8]]


salaryPredict = model.predict(newEmployee)
print(f"O salário previsto pelo modelo é de R$ {salaryPredict[0][0]:.2f} mil.")
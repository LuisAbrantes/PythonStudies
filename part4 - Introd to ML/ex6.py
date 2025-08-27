# As importações que você vai precisar
import pandas as pd
import io
from sklearn.neighbors import KNeighborsRegressor

dados_sorvetes_csv = """temperatura_celsius,unidades_vendidas
20,150
25,210
28,260
30,300
33,350
35,380
"""
dfSorvetes = pd.read_csv(dados_sorvetes_csv)

x = dfSorvetes[["temperatura_celsius"]]
y = dfSorvetes[["unidades_vendidas"]]

modelo = KNeighborsRegressor()
modelo.fit(x,y)
temposFuturos = [[26], [31], [38]]
vendasFuturas = modelo.predict(temposFuturos)

print(f"O preço da pizza previsto pelo modelo é de R$ {vendasFuturas[0][0]:.2f}.")
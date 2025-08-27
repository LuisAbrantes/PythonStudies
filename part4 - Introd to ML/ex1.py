import pandas as pd
import io # Usado para simular um arquivo

# Imagine que o texto abaixo é o conteúdo do arquivo "casas.csv"
dados_csv = """area_m2,n_quartos,preco_milhares
70,2,250
90,3,310
65,2,240
120,3,450
150,4,580
"""

# Em um caso real, você faria: df = pd.read_csv("caminho/para/casas.csv")
# Mas vamos ler a nossa string para simular:
df_casas = pd.read_csv(io.StringIO(dados_csv))

print("--- DataFrame carregado do CSV ---")
print(df_casas)

# Vendo as primeiras linhas
print("\n--- Saída do .head() ---")
print(df_casas.head())

# Vendo as estatísticas
print("\n--- Saída do .describe() ---")
print(df_casas.describe())

# Qual é a área média (mean) das casas no nosso conjunto de dados? 99m^2
# Qual é o preço máximo (max), em milhares, de uma casa nesse conjunto de dados? $580
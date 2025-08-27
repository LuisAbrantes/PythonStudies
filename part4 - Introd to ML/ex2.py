# PASSO 1: IMPORTAR AS BIBLIOTECAS
import pandas as pd
import io
from sklearn.linear_model import LinearRegression

# --- Início do nosso "Projeto" ---

# PASSO 2: CARREGAR OS DADOS
# No mundo real, isso seria: df_casas = pd.read_csv('casas.csv')
print("--- 1. Carregando Dados ---")
dados_csv = """area_m2,n_quartos,preco_milhares
70,2,250
90,3,310
65,2,240
120,3,450
150,4,580
"""
df_casas = pd.read_csv(io.StringIO(dados_csv))
print("Dados carregados com sucesso!\n")


# PASSO 3: PREPARAR OS DADOS (SEPARAR EM FEATURES E TARGET)
print("--- 2. Preparando os Dados ---")
X = df_casas[['area_m2', 'n_quartos']] # As 'pistas'
y = df_casas['preco_milhares']        # O 'alvo'
print("Dados separados em X (features) e y (target).\n")


# PASSO 4: ESCOLHER E TREINAR O MODELO
print("--- 3. Treinando o Modelo ---")
modelo = LinearRegression() # Criamos o modelo
modelo.fit(X, y)            # Treinamos o modelo com nossos dados
print("Modelo treinado com sucesso!\n")


# PASSO 5: FAZER UMA PREVISÃO COM DADOS NOVOS
print("--- 4. Fazendo uma Previsão ---")
# Vamos imaginar uma nova casa que o modelo nunca viu antes.
# Por exemplo, uma casa com 110 m² e 3 quartos.
# Precisamos passar os dados no mesmo formato de X (uma lista de listas ou um DataFrame).
nova_casa = [[200, 5]]

# Usamos o método .predict() para obter a previsão do modelo
preco_previsto = modelo.predict(nova_casa)

print(f"Para uma casa de {nova_casa[0][0]}m² e {nova_casa[0][1]} quartos...")
# O resultado vem em um array, então pegamos o primeiro elemento com [0]
print(f"O preço previsto pelo modelo é de R$ {preco_previsto[0]:.2f} mil.")
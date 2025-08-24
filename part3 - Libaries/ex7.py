# 2 - Pandas
# a) Crie um DataFrame do Pandas a partir deste dicionário.
# b) Adicione uma nova coluna chamada 'Nota_Final' 
# que seja a média das notas G1 e G2: (Nota_G1 + Nota_G2) / 2.
# c) Filtre e mostre apenas os estudantes que foram aprovados, 
# ou seja, que têm Nota_Final maior ou igual a 7.0 E (&) menos de 5 faltas.

# 3 - Matplotlib / Seaborn
# Usando o DataFrame de estudantes do exercício anterior, 
# você quer criar uma visualização para entender se existe uma 
# relação entre o número de faltas de um aluno e sua nota final.

import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt

dados_estudantes = {
    'Nome': ['Ana', 'Bruno', 'Carla', 'Daniel'],
    'Nota_G1': [8.5, 7.0, 9.5, 6.0],
    'Nota_G2': [9.0, 8.0, 9.5, 7.5],
    'Faltas': [2, 5, 0, 8]
}

dfDados = pd.DataFrame(dados_estudantes)

dfDados["NotaFinal"] = (dfDados['Nota_G1']+dfDados['Nota_G2']) / 2

condition = (dfDados["NotaFinal"] >= 7.0) & (dfDados["Faltas"] < 5)
approvedStudents = dfDados[condition]

print(f"Os alunos aprovados foram: \n{approvedStudents}")


sns.scatterplot(x="Faltas", y="NotaFinal", data=dfDados)
plt.title("Como as faltas afetam as notas finais dos estudantes.")
plt.show()
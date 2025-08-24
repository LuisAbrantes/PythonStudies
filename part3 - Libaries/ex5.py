import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

dados_estudo = {
    'horas_estudo': [2.5, 5.1, 3.2, 8.5, 6.5, 9.2, 5.5, 7.0],
    'nota_prova':   [60,  75,  68,  92,  85,  98,  78,  88]
}
df_notas = pd.DataFrame(dados_estudo)

sns.scatterplot(x="horas_estudo", y="nota_prova", data=df_notas)
plt.title("Horas de estudo por nota de prova")
plt.show()
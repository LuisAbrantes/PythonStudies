# Montagem de matrizes e tensores + extração de valores com numpy

import numpy as np

dados_vendas = np.array([
    [10, 15, 12],  # Linha 0
    [20, 22, 25]   # Linha 1
])
# Coluna 0, 1, 2
specificData = dados_vendas[1,1]
specificColumn = dados_vendas[:, 2]
print(specificColumn)
print(specificData)
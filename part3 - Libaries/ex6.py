#RECAP exercises start here - Numpy

# Você tem dados de altura (em metros) de um grupo de pessoas em uma lista.

# alturas_lista = [1.75, 1.80, 1.65, 1.90, 1.72]

# Sua Tarefa:
# a) Converta a alturas_lista para um array NumPy.
# b) Crie um novo array chamado alturas_em_cm que contenha as alturas convertidas para centímetros (dica: altura em m * 100). Faça isso em uma única operação vetorizada.
# c) Acesse e imprima a terceira altura (índice 2) do array original em metros.


import numpy as np

highList = [1.75, 1.80, 1.65, 1.90, 1.72]
arrayHighList = np.array(highList)
highListCm = arrayHighList * 100

dataAsked = arrayHighList[2]
print(dataAsked)
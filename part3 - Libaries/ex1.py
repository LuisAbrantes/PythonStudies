import numpy as np

pesos = [70.5, 82.1, 65.4, 91.3]
alturas = [1.75, 1.81, 1.69, 1.79]

# 1. Converta as duas listas para arrays NumPy.
array_pesos = np.array(pesos)
array_alturas = np.array(alturas)

# 2. Calcule os IMCs de todos de uma vez usando as operações vetorizadas.
#    Lembre-se: altura² é o mesmo que altura * altura.
array_imc = array_pesos / (array_alturas*array_alturas)

print(f"Pesos: {array_pesos}")
print(f"Alturas: {array_alturas}")
print(f"Array de IMCs calculados: {array_imc}")
# Você tem uma lista de nomes e quer ordená-la pelo comprimento de cada nome, do menor para o maior. 
# A função sorted() do Python aceita um argumento key para definir o critério de ordenação.
# nomes = ["Anna", "Abraham", "Robert", "Zihao", "Jooohn"]
# Como você usaria a função sorted() com uma função lambda para ordenar essa lista pelo comprimento dos nomes?

names = ["Anna", "Abraham", "Robert", "Zihao", "Jooohn"]
ordedNames = sorted(names, key = lambda name: len(name))
print(ordedNames)
    

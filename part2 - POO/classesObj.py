# Crie uma classe chamada Filme. Ela deve ter:

# Um método __init__ que recebe titulo, diretor e ano_lancamento.

# Um atributo chamado assistido, que deve sempre começar como False.

# Um método chamado marcar_como_assistido() que muda o valor de assistido para True.

# Um método mostrar_info() que imprime uma string formatada com todas as informações do filme, 
# incluindo se ele foi assistido ou não. 
# Ex: Título: Interestelar, Diretor: Christopher Nolan (2014) - Assistido: Sim.

class Film:
    def __init__(self, title, director, year):
        self.title = title
        self.director = director
        self.year = year 
        self.watched = False
    
    def watch(self):
        self.watched = True
        
    def showInfo(self):
        watchedStr = "Yes" if self.watched else "No"
        print(f"Film: {self.title};\n Director: {self.director} ({self.year} - Watched: {watchedStr}); ")
        
theForge = Film("The Forge", "Alex Kendrick", 2024)
theForge.showInfo()
theForge.watch()
theForge.showInfo()
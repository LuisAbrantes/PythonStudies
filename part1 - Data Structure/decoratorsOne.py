# Imagine que você tem funções que só podem ser executadas em horário comercial (simulado). 
# Escreva um decorador @horario_comercial que, antes de executar uma função, verifica uma variável hora_atual. 
# Se hora_atual estiver entre 9 e 18, ele executa a função. Caso contrário, ele imprime "Fora do horário de serviço!".

# Simulação da hora
hora_atual = 15

# Seu decorador aqui
def horario_comercial(function):
    def wrapper():
        if hora_atual>=9 and hora_atual<=18:
            function()
        else:
            print("Out of service.")
            
    return wrapper
        

@horario_comercial
def fazer_relatorio():
    print("Gerando relatório...")

fazer_relatorio() # Deve imprimir "Fora do horário de serviço!"
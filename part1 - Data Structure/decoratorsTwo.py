# Novo Desafio: O Dobrador de Resultados
# Vamos criar um decorador @dobrar_resultado. A tarefa dele é simples:

# Executar uma função que retorna um número.

# Pegar esse número.

# Dobrar o valor dele.

# Retornar o novo valor dobrado.


# Seu decorador aqui
def dobrar_resultado(funcao_original):
    def embrulho():
        # 1. Chame a função original e guarde o número que ela retorna em uma variável.
        n = funcao_original()
        
        # 2. Crie uma nova variável com o dobro desse número.
        d = n*2
        
        # 3. Retorne a nova variável com o resultado dobrado.
        return d
        
    return embrulho


@dobrar_resultado
def obter_dez():
    return 10

# --- Teste ---
# Se o decorador funcionar, a variável 'resultado_final' deverá conter o valor 20.
resultado_final = obter_dez()
print(f"O resultado final obtido foi: {resultado_final}")
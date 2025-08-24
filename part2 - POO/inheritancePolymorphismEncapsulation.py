# Parte A (Encapsulamento): Modifique a classe Conta para que o atributo saldo se torne "protegido" (usando o _). 
# Garanta que todos os métodos da classe usem o novo nome (_saldo).

# Parte B (Herança e Polimorfismo): Crie uma classe ContaPoupanca que herda de Conta. 
# A ContaPoupanca tem uma regra diferente para saques: ela cobra uma taxa de R$ 2,00 por cada saque. 
# Você deve sobrescrever o método sacar() para implementar essa nova lógica. 
# O novo método deve verificar se o saldo é suficiente para cobrir o saque + a taxa.

class Conta:
    def __init__(self, titular, saldo_inicial):
        self.titular = titular
        self._saldo = saldo_inicial # Este atributo deve ser protegido

    def depositar(self, valor):
        self._saldo += valor
        print("Depósito realizado.")

    def sacar(self, valor):
        if valor <= self._saldo:
            self._saldo -= valor
            print("Saque realizado.")
            return True
        else:
            print("Saldo insuficiente.")
            return False
        
class ContaPoupanca(Conta):
        def sacar(self, valor):
            tax = 2
            if valor + tax <= self._saldo:
                self._saldo -= valor + tax
                print("Saque realizado. ")
                return True
            else:
                print("Saldo insuficiente.")
                return False
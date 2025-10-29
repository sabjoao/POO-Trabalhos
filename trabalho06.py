from abc import ABC
from datetime import date

class Conta:
    def __init__(self, nroConta, nome, limite, senha):
        self.__nroConta = nroConta
        self.__nome = nome
        self.__limite = limite
        self.__senha = senha
        self._transacoes = []
        

    @property
    def nroConta(self):
        return self.__nroConta
    
    @nroConta.setter
    def nroConta(self, nroConta):
        self.__nroConta = nroConta

    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, limite):
        self.__limite = limite

    @property
    def senha(self):
        return self.__senha
    
    @senha.setter
    def senha(self, senha):
        self.__senha = senha


    def calculaSaldo(self):
        saldo = self.__limite
        for t in self._transacoes:
            if isinstance(t, Deposito):
                saldo += t.valor
            elif isinstance(t, Saque):
                saldo -= t.valor
            elif isinstance(t, Transferencia):
                if t.tipoTransf == "D":
                    saldo -= t.valor
                else:
                    saldo += t.valor
        return saldo

    def adicionaDeposito(self, valor, data, nomeDepositante):
        dep = Deposito(valor, data, nomeDepositante)
        self._transacoes.append(dep)
        

    def adicionaSaque(self, valor, data, senha):
        if senha != self.__senha:
            return False
        if self.calculaSaldo() - valor < 0:
            return False
        saq = Saque(valor, data, senha)
        self._transacoes.append(saq)
        return True
        

    def adicionaTransf(self, valor, data, senha, contaFavorecida):
        if self.calculaSaldo() - valor < 0:
            return False
        
        if senha != self.__senha:
            return False
        
        transfDeb = Transferencia(valor, data, senha, "D")
        self._transacoes.append(transfDeb)
        
        transfCred = Transferencia(valor, data, senha, "C")
        contaFavorecida._transacoes.append(transfCred)
        

        return True
        

class Transacoes(ABC):
    def __init__(self, valor, data):
      self.__valor = valor
      self.__data = data
      
    @property
    def valor(self):
         return self.__valor
      
    @valor.setter
    def valor(self, valor):
        self.__valor = valor

    @property
    def data(self):
       return self.__data
    
    @data.setter
    def data(self, data):
       self.__data = data



class Deposito(Transacoes):
    def __init__(self, valor, data, nomeDepositante):
        super().__init__(valor, data)
        self.__nomeDepositante = nomeDepositante

    @property
    def nomeDepositante(self):
        return self.__nomeDepositante
    
    @nomeDepositante.setter
    def nomeDepositante(self, nomeDepositante):
        self.__nomeDepositante = nomeDepositante



class Saque(Transacoes):
    def __init__(self, valor, data, senha):
        super().__init__(valor, data)
        self.__senha = senha

    @property
    def senha(self):
       return self.__senha

    @senha.setter
    def senha(self, senha):
        self.__senha = senha

class Transferencia(Transacoes):
    def __init__(self, valor, data, senha, tipoTransf):
        super().__init__(valor, data)
        self.__senha = senha
        self.__tipoTransf = tipoTransf

    @property
    def senha(self):
       return self.__senha

    @senha.setter
    def senha(self, senha):
        self.__senha = senha

    @property
    def tipoTransf(self):
        return self.__tipoTransf
    
    @tipoTransf.setter
    def tipoTransf(self, tipoTransf):
        self.__tipoTransf = tipoTransf









if __name__ == "__main__":
 c1 = Conta(1234, 'Jose da Silva', 1000, 'senha1')
 c1.adicionaDeposito(5000, date.today(), 'Antonio Maia')
 if c1.adicionaSaque(2000, date.today(), 'senha1') == False:
    print('Não foi possível realizar o saque no valor de 2000')
 if c1.adicionaSaque(1000, date.today(), 'senha-errada') == False: # deve falhar
    print('Não foi possível realizar o saque no valor de 1000')

 c2 = Conta(4321, 'Joao Souza', 1000, 'senha2')
 c2.adicionaDeposito(3000, date.today(), 'Maria da Cruz')
 if c2.adicionaSaque(1500, date.today(), 'senha2') == False:
    print('Não foi possível realizar o saque no valor de 1500')
 if c2.adicionaTransf(5000, date.today(), 'senha2', c1) == False: # deve falhar
    print('Não foi possível realizar a transf no valor de 5000')
 if c2.adicionaTransf(800, date.today(), 'senha2', c1) == False:
    print('Não foi possível realizar a transf no valor de 800')
print('--------')
print('Saldo de c1: {}'.format(c1.calculaSaldo())) # deve imprimir 4800
print('Saldo de c2: {}'.format(c2.calculaSaldo())) # deve imprir 1700
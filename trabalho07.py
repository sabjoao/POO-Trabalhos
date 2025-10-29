from abc import ABC, abstractmethod

class Vendedor(ABC):
    def __init__(self, codigo, nome):
        self.__codigo = codigo
        self.__nome = nome
        self._vendas = []

    @property
    def codigo(self):
        return self.__codigo
        
    @codigo.setter
    def codigo(self, codigo):
        self.__codigo = codigo

    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @abstractmethod
    def getDados():
        pass

    @abstractmethod
    def calculaRenda(self, mes, ano):
        pass

    def adicionaVenda(self, codImovel, mes, ano, valor):
        ven = Venda(codImovel, mes, ano, valor)
        self._vendas.append(ven)

    

class Contratado(Vendedor):
    def __init__(self, codigo, nome, salarioFixo, nroCartTrabalho):
        super().__init__(codigo, nome)
        self.__nroCartTrabalho = nroCartTrabalho
        self.__salarioFixo = salarioFixo
        

    @property
    def nroCartTrabalho(self):
        return self.__nroCartTrabalho

    @nroCartTrabalho.setter
    def nroCartTrabalho(self, nroCartTrabalho):
        self.__nroCartTrabalho = nroCartTrabalho

    @property
    def salarioFixo(self):
        return self.__salarioFixo
    
    @salarioFixo.setter
    def salarioFixo(self, salarioFixo):
        self.__salarioFixo = salarioFixo

    def getDados(self):
        return f"Nome: {self.nome} - Nro carteira: {self.nroCartTrabalho}"

    def calculaRenda(self, mes, ano):
        renda = 0
        for t in self._vendas:
            if t.mesVenda == mes and t.anoVenda == ano:
                renda = renda +  (t.valorVenda * 0.01)
        return renda + self.salarioFixo
    

class Venda:
    def __init__(self, codImovel, mesVenda, anoVenda, valorVenda):
        self.__codImovel = codImovel
        self.__mesVenda = mesVenda
        self.__anoVenda = anoVenda
        self.__valorVenda = valorVenda

    @property
    def codImovel(self):
        return self.__codImovel
    
    @codImovel.setter
    def codImovel(self, codImovel):
        self.__codImovel = codImovel

    @property
    def mesVenda(self):
        return self.__mesVenda
    
    @mesVenda.setter
    def mesVenda(self, mesVenda):
        self.__mesVenda = mesVenda

    @property
    def anoVenda(self):
        return self.__anoVenda
    
    @anoVenda.setter
    def anoVenda(self, anoVenda):
        self.__anoVenda = anoVenda

    @property
    def valorVenda(self):
        return self.__valorVenda
    
    @valorVenda.setter
    def valorVenda(self, valorVenda):
        self.__valorVenda = valorVenda



class Comissionado(Vendedor):
    def __init__(self, codigo, nome, nroCPF, comissao):
        super().__init__(codigo, nome)
        self.__nroCPF = nroCPF
        self.__comissao = comissao

    @property
    def nroCPF(self):
        return self.__nroCPF
    
    @nroCPF.setter
    def nroCPF(self, nroCPF):
        self.__nroCPF = nroCPF

    @property
    def comissao(self):
        return self.__comissao
    
    @comissao.setter
    def comissao(self, comissao):
        self.__comissao = comissao

    def getDados(self):
        return f"Nome: {self.nome} - Nro CPF: {self.nroCPF}"

    def calculaRenda(self, mes, ano):
        renda = 0
        for t in self._vendas:
            if t.mesVenda == mes and t.anoVenda == ano:
                renda = renda + (t.valorVenda * (self.__comissao*0.01))
        return renda 
if __name__ == "__main__":
    funcContratado = Contratado(1001, 'João da Silva', 2000, 1234)
    funcContratado.adicionaVenda(100, 3, 2022, 200000)
    funcContratado.adicionaVenda(101, 3, 2022, 300000)
    funcContratado.adicionaVenda(102, 4, 2022, 600000)
    funcComissionado = Comissionado(1002, 'José Santos', 4321, 5)
    funcComissionado.adicionaVenda(200, 3, 2022, 200000)
    funcComissionado.adicionaVenda(201, 3, 2022, 400000)
    funcComissionado.adicionaVenda(202, 4, 2022, 500000)
    listaFunc = [funcContratado, funcComissionado]
    for func in listaFunc:
        print (func.getDados())
        print ("Renda no mês 3 de 2022: ")
        print (func.calculaRenda(3, 2022))

        
        

    


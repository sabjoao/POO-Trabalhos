from abc import ABC, abstractmethod

class Funcionario(ABC):
    def __init__(self, codigo, nome):
        self.__codigo = codigo
        self.__nome = nome
        self._ponto = {}
    

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

    def adicionaPonto(self, mes, ano, nroFaltas, nroAtrasos):
        self._ponto[(mes, ano)] = PontoFunc(mes, ano, nroFaltas, nroAtrasos)

    def lancaFaltas(self, mes, ano, faltas):
        ponto = self._ponto[(mes, ano)]
        ponto.lancaFaltas(faltas)

    def lancaAtrasos(self, mes, ano, atrasos):
        ponto = self._ponto[(mes, ano)]
        ponto.lancaAtrasos(atrasos)

    @abstractmethod
    def calculaSalario(self, mes, ano):
        pass

    @abstractmethod
    def calculaBonus(self, mes, ano):
        pass

    def imprimeFolha(self, mes, ano):
        ponto = self._ponto[(mes, ano)]
        print(f"Código: {self.__codigo}")
        print(f"Nome: {self.__nome}")
        salarioProf = self.calculaSalario(mes, ano)
        print(f"Salário líquido: {salarioProf:.2f}")
        bonus = self.calculaBonus(mes, ano)
        print(f"Bonus: {bonus:.2f}")
        


class PontoFunc:
    def __init__(self, mes, ano, nroFaltas, nroAtrasos):
        self.__mes = mes
        self.__ano = ano
        self.__nroFaltas = nroFaltas
        self.__nroAtrasos = nroAtrasos

    @property
    def mes(self):
        return self.__mes
    
    @mes.setter
    def mes(self, mes):
        self.__mes = mes

    @property
    def ano(self):
        return self.__ano
    
    @ano.setter
    def codigo(self, ano):
        self.__ano = ano

    @property
    def nroFaltas(self):
        return self.__nroFaltas
    
    @nroFaltas.setter
    def nroFaltas(self, nroFaltas):
        self.__nroFaltas = nroFaltas

    @property
    def nroAtrasos(self):
        return self.__nroAtrasos
    
    @nroAtrasos.setter
    def nroAtrasos(self, nroAtrasos):
        self.__nroAtrasos = nroAtrasos

    def lancaFaltas(self, faltas):
        self.__nroFaltas += faltas

    def lancaAtrasos(self, atrasos):
        self.__nroAtrasos += atrasos


class Professor(Funcionario):
    def __init__(self, codigo, nome, titulacao, salarioHora, nroAulas):
        super().__init__(codigo, nome)
        self.__titulacao = titulacao
        self.__salarioHora = salarioHora
        self.__nroAulas = nroAulas

    @property
    def titulacao(self):
        return self.__titulacao
        
    @titulacao.setter
    def titulacao(self, titulacao):
        self.__titulacao = titulacao

    @property
    def salarioHora(self):
        return self.__salarioHora
        
    @salarioHora.setter
    def salarioHora(self, salarioHora):
        self.__salarioHora = salarioHora

    @property
    def nroAulas(self):
        return self.__nroAulas
        
    @nroAulas.setter
    def nroAulas(self, nroAulas):
        self.__nroAulas = nroAulas

    def calculaSalario(self, mes, ano):
        ponto = self._ponto[(mes, ano)]
        salarioProf = (self.__salarioHora * self.__nroAulas) - (self.__salarioHora * ponto.nroFaltas)
        return salarioProf

    def calculaBonus(self, mes, ano):
        ponto = self._ponto[(mes, ano)]
        if(ponto.nroAtrasos == 0):
            bonus =  self.calculaSalario(mes, ano) * 0.10
            return bonus
        else:
            descontoBonus = (0.10 - (ponto.nroAtrasos * 0.01))
            bonus = self.calculaSalario(mes, ano) * descontoBonus          
            return bonus
        
class TecAdmin(Funcionario):
    def __init__(self, codigo, nome, funcao, salarioMensal):
        super().__init__(codigo, nome)
        self.__funcao = funcao
        self.__salarioMensal = salarioMensal 

    @property
    def funcao(self):
        return self.__funcao
    
    @funcao.setter
    def funcao(self, funcao):
        self.__funcao = funcao

    @property
    def salarioMensal(self):
        return self.__salarioMensal
    
    @salarioMensal.setter
    def salarioMensal(self, salarioMensal):
        self.__salarioMensal = salarioMensal

    def calculaSalario(self, mes, ano):
        ponto = self._ponto[(mes, ano)]
        salario =  self.__salarioMensal - ((self.__salarioMensal/30)* ponto.nroFaltas)
        return salario
    
    def calculaBonus(self, mes, ano):
        ponto = self._ponto[(mes, ano)]
        if(ponto.nroAtrasos == 0):
            bonus =  self.calculaSalario(mes, ano) * 0.08
            return bonus
        else:
            descontoBonus = (0.08 - (ponto.nroAtrasos * 0.01))
            bonus = self.calculaSalario(mes, ano) * descontoBonus          
            return bonus


if __name__ == "__main__":
    funcionarios = []
    prof = Professor(1, "Joao", "Doutor", 45.35, 32)
    prof.adicionaPonto(4, 2021, 0, 0)
    prof.lancaFaltas(4, 2021, 2)
    prof.lancaAtrasos(4, 2021, 3)
    funcionarios.append(prof)
    tec = TecAdmin(2, "Pedro", "Analista Contábil", 3600)
    tec.adicionaPonto(4, 2021, 0, 0)
    tec.lancaFaltas(4, 2021, 3)
    tec.lancaAtrasos(4, 2021, 4)
    funcionarios.append(tec)
    for func in funcionarios:
        func.imprimeFolha(4, 2021)
        print()

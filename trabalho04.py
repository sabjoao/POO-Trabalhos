from abc import ABC, abstractmethod

class EmpDomestica(ABC):
    def __init__(self, nome, telefone):
        self.__nome = nome
        self.__telefone = telefone 

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def telefone(self):
        return self.__telefone
    
    @telefone.setter
    def telefone(self, telefone):
        self.__telefone = telefone
    
    @abstractmethod
    def get_salario(self):
        pass

class Horista(EmpDomestica):
    def __init__(self, nome, telefone, HorasTrabalhadas, ValorPorHora):
        super().__init__(nome, telefone)
        self.__HorasTrabalhadas = HorasTrabalhadas
        self.__ValorPorHora = ValorPorHora

    @property
    def HorasTrabalhadas(self):
        return self.__HorasTrabalhadas
    
    @HorasTrabalhadas.setter
    def HorasTrabalhadas(self, HorasTrabalhadas):
        self.__HorasTrabalhadas = HorasTrabalhadas

    @property 
    def ValorPorHora(self, ValorPorHora):
        self.__ValorPorHora = ValorPorHora

    @ValorPorHora.setter
    def ValorPorHora(self, ValorPorHora):
        self.__ValorPorHora = ValorPorHora

    def get_salario(self):
        return self.__HorasTrabalhadas * self.__ValorPorHora
    
class Diarista(EmpDomestica):
    def __init__(self, nome, telefone, DiasTrabalhados, ValorPorDia):
        super().__init__(nome,telefone)
        self.__DiasTrabalhados = DiasTrabalhados
        self.__ValorPorDia = ValorPorDia

    @property
    def DiasTrabalhados(self):
        return self.__DiasTrabalhados
    
    @DiasTrabalhados.setter
    def DiasTrabalhados(self, DiasTrabalhados):
        self.__DiasTrabalhados = DiasTrabalhados

    @property   
    def ValorPorDia(self):
        return self.__ValorPorDia
    
    @ValorPorDia.setter
    def ValorPorDia(self, ValorPorDia):
        self.__ValorPorDia = ValorPorDia

    def get_salario(self):
        return self.__DiasTrabalhados * self.__ValorPorDia
    
class Mensalista(EmpDomestica):
    def __init__(self, nome, telefone, ValorMensal):
        super().__init__(nome, telefone)
        self.__ValorMensal = ValorMensal

    @property
    def ValorMensal(self):
        return self.__ValorMensal
    
    @ValorMensal.setter
    def ValorMensal(self, ValorMensal):
        self.__ValorMensal = ValorMensal

    def get_salario(self):
        return self.__ValorMensal
    
if __name__ == "__main__":
    listaEmpregadas = []

    emp1 = Horista('Maria', 123, 160, 12)
    listaEmpregadas.append(emp1)
    
    emp2 = Diarista('Eduarda', 456, 20, 65)
    listaEmpregadas.append(emp2)
    
    emp3 = Mensalista('Isabella', 789, 1200)
    listaEmpregadas.append(emp3)

    for empregada in listaEmpregadas:
        print('Nome: {} - Salário: {}'.format(empregada.nome, empregada.get_salario()))

    for empregada in listaEmpregadas:
        salmaio = 0
        sal = empregada.get_salario()
        if salmaio < sal:
            salmaio = sal
            name = empregada.nome
            tel = empregada.telefone

    print('A melhor empregada para ser contratada é a {}, seu número de telefone é o {}, ela ira receber {} R$ de salário' .format(name, tel, salmaio))


from abc import ABC, abstractmethod

class TitulacaoDoutor(Exception):
    pass

class Idade30(Exception):
    pass

class CursoAluno(Exception):
    pass

class Idade18(Exception):
    pass

class CPFigual(Exception):
    pass

class Pessoa(ABC):
    def __init__(self, nome, endereco, idade, cpf):
        self.__nome = nome
        self.__endereco = endereco
        self.__idade = idade
        self.__cpf = cpf

    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def endereco(self):
        return self.__endereco
    
    @endereco.setter
    def endereco(self, endereco):
        self.__endereco = endereco

    @property
    def idade(self):
        return self.__idade
    
    @idade.setter
    def idade(self, idade):
        self.__idade = idade
    
    @property
    def cpf(self):
        return self.__cpf
    
    @cpf.setter
    def cpf(self, cpf):
        self.__cpf = cpf

    @abstractmethod
    def printDescricao():
        pass


class Professor(Pessoa):
    def __init__(self, nome, endereco, idade, cpf, titulacao):
        super().__init__(nome, endereco, idade, cpf)
        self.__titulacao = titulacao

    @property
    def titulacao(self):
        return self.__titulacao
    
    @titulacao.setter
    def titulacao(self, titulacao):
        self.__titulacao = titulacao

    def printDescricao(self):
        print(f"Nome: {self.nome}")
        print(f"Endereço: {self.endereco}")
        print(f"Idade: {self.idade}")
        print(f"CPF: {self.cpf}")
        print(f"Titulação: {self.titulacao}")

class Aluno(Pessoa):
    def __init__(self, nome, endereco, idade, cpf, curso):
        super().__init__(nome, endereco, idade, cpf)
        self.__curso = curso

    @property
    def curso(self):
        return self.__curso
    
    @curso.setter
    def aluno(self, curso):
        self.__curso = curso

    def printDescricao(self):
        print(f"Nome: {self.nome}")
        print(f"Endereço: {self.endereco}")
        print(f"Idade: {self.idade}")
        print(f"CPF: {self.cpf}")
        print(f"Titulação: {self.curso}")

if __name__ == "__main__":
    pessoas = [
        Professor("Carlos Silva", "Rua das Palmeiras, 120", 45, "11111111111", "doutor"), 
        Professor("Ana Costa", "Av. Brasil, 450", 38, "22222222222", "mestre"), #
        Professor("Paulo Souza", "Rua Afonso Pena, 33", 29, "33333333333", "doutor"), #
        Professor("Maria Santos", "Rua das Palmeiras, 120", 52, "11111111111", "doutor"), #
        Aluno("João Pereira", "Rua das Laranjeiras, 10", 19, "44444444444", "CCO"), 
        Aluno("Fernanda Lima", "Av. Atlântica, 220", 22, "55555555555", "SIN"), 
        Aluno("Rafael Torres", "Rua Goiás, 89", 17, "66666666666", "CCO"), #
        Aluno("Luiza Almeida", "Rua XV de Novembro, 300", 20, "77777777777", "ADM"), #
        Aluno("Pedro Martins", "Rua das Laranjeiras, 10", 21, "44444444444", "SIN") #
        ]
    Cadastros = {}

    for t in pessoas:
        try:
            if isinstance(t, Aluno):
                if t.curso != "CCO" and t.curso != "SIN":
                    raise CursoAluno
                elif t.idade < 18:
                    raise Idade18
                elif t.cpf in Cadastros:
                    raise CPFigual
                else:
                    Cadastros[t.cpf] = t
                    
            else:
                if t.titulacao != "doutor":
                    raise TitulacaoDoutor
            
                elif t.idade < 30:
                    raise Idade30
            
                elif t.cpf in Cadastros:
                    raise CPFigual
                else:
                    Cadastros[t.cpf] = t
        except CursoAluno:
            print("O curso não é nem SIN nem CCO")
            print()

        except Idade18:
            print("A idade do aluno é menor que 18")
            print()
        except CPFigual:
            print("O CPF já está cadastrado")
            print()
        except TitulacaoDoutor:
            print("O professor não é doutor")
            print()
        except Idade30:
            print("O professor tem menos de 30 anos")
            print()

    for cpf, x in Cadastros.items():
        x.printDescricao()
        print()
    
        

        
    
    

    



        

    




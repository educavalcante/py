
class Funcionario:
    def __init__(self, nome, cpf, salario):
        self._nome = nome
        self._cpf = cpf
        self._salario = salario
    
    def salario_Liquido(self, itens_descontos):
        liquido = self._salario
        for desconto in itens_descontos:
            liquido -= desconto
        return liquido
    
class Gerente(Funcionario):
    def __init__(self,nome, cpf, salario, senha, ger):
        super().__init__(nome, cpf, salario)
        self.__senha = senha
        self.__ger = ger
        
    @property
    def senha(self):
        return self.__senha
    @senha.setter
    def senha(self, senha):
        self.__senha = senha
    
    @property
    def ger(self):
        return self.__ger
    @ger.setter
    def ger(self, ger):
        self.__ger = ger

    
        
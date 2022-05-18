class Dog:
    def __init__(self, raca, idade, nome=None): #posiciais primeiro nomeados depois
        print(f'Eu sou o sefl: {self}')
        self.nome = nome #publico
        self._raca = raca #protegido a classe mae e filhas acessam acessar atraves dos metodos getes e seteres
        self.__idade = idade #privado somente a classe acessa acessar atraves dos metodos getes e seteres
        
puppy = Dog(nome='rex', idade=5, raca="pastor alemao")
boomer = Dog(nome='boomer', raca="pudle", idade=1)
print(puppy.nome)
print(boomer.nome) 
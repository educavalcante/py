class Cliente:
    def __init__(self, nome, email, senha, endereco):
        self.__nome = nome
        self.__email = email
        self.__senha = senha
        self.__endereco = endereco
        
    @property
    def nome(self):
        return self.__nome
    @nome.setter
    def nome(self, nome):
        self.__nome = nome
    
    @property
    def email(self):
        return self.__email
    @email.setter
    def email(self, email):
        self.__email = email
    
    @property
    def senha(self):
        return self.__senha
    @email.setter
    def senha(self, senha):
        self.__senha = senha
    
    @property
    def endereco(self):
        return self.__endereco
    @endereco.setter
    def endereco(self, endereco):
        self.__endereco = endereco
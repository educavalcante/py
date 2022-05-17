from endereco import Endereco
from cliente import Cliente
#dados do cliente
nome = input("informe o seu nome: ")
email = input("informe o seu email: ")
senha = input("informe o seu senha: ")

#dados endereco do cliente
cep = input("informe o seu cep: ")
rua = input("informe o seu rua: ")
numero = input("informe o seu numero: ")
cidade = input("informe o seu cidade: ")
estado = input("informe o seu estado: ")
pais = input("informe o seu pais: ")

#criando o endereco
endereco1 = Endereco(cep, rua, numero, cidade, estado, pais)

#criando um cliente
cliente1 = Cliente(nome, email, senha, endereco1)
print("nome: ", cliente1.nome)
print("Email: ", cliente1.email)
print("Endereco: ", cliente1.endereco.rua,",", cliente1.endereco.pais)
                   
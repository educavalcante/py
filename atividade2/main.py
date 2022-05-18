from gerente import Gerente


gerente = Gerente("Ana", "4545455", 25000, "12345678", 12)
plano_saude = 300
inss = 280
i_r = 500
lista_descontos = [plano_saude, inss, i_r]
salario_Liquido = gerente.salario_Liquido(lista_descontos)
print(salario_Liquido) 
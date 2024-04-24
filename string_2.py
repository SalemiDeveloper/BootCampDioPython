nome = "Pedro"
idade = 22
profissao = "Estagiário"
linguagem = "Python"
dados = {"nome": "Pedro", "idade": 22}
saldo = 45.435

#Método 1 não utilizado atualmente
print("Nome : %s  Idade: %d" %(nome, idade))

#Método 2
print("Nome: {}  Idade: {}".format(nome, idade))
print("Nome: {1}  Idade: {0}".format(nome, idade))
print("Nome: {1}  Idade: {0}  Nome: {1} {1}".format(idade, nome))
print("Nome: {name}  Idade: {age}".format(age=idade, name=nome))
print("Nome: {nome}  Idade: {idade}".format(**dados))

#Método 3
print(f"Nome: {nome}  Idade: {idade}")
print(f"Nome: {nome}  Idade: {idade}  Saldo: {saldo:.2f}")
print(f"Nome: {nome}  Idade: {idade}  Saldo: {saldo:10.2f}") #esse 10 é para espaçamento

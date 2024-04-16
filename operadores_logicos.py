saldo = 1000
saque = 200
limite = 100

#AND = para ser True tudo tem que ser True
saldo >= saque and saque <= limite #vai retornar "False" pois saque não é menor ou igual ao limite
#no "and" os dois tem que ser verdadeiros para retornar "True"

#OR = para ser True apenas um tem que ser True
saldo >= saque or saque <= limite #vai retornar "True" pois mesmo que os dois não sejam verdadeiros, um deles é
#no "or" para ser verdadeiro, apenas um deles precisa ser. Porém, para ser falso, os dois precisam ser



contato_emergencia = []

#NEGAÇÃO
not 1000 > 1500 #1000 nao é maior que 1500, logo vai retornar "True"

not contato_emergencia #é uma lista vazia, então vai retornar "True" já que não existe nada na lista

not "saque 1500" #a string é verdadeira, então vai retornar "False"

not "" #vai retornar "True"

#Em python uma sequência vazia é considerada FALSE, por isso a lista vazia e a string vazia no NOT vai retornar "True"



conta_especial = True

#PARÊNTESES
exp = saldo >= saque and saque <= limite or conta_especial and saldo >= saque #vai retornar "True"

exp_2 = (saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque) #mesma coisa que o de cima, porém muito mais legível

print(exp)
print(exp_2)

conta_normal_com_saldo_suficiente = (saldo >= saque and saque <= limite)
conta_especial_com_saldo_suficiente = (conta_especial and saldo >= saque)

exp_3 = conta_normal_com_saldo_suficiente or conta_especial_com_saldo_suficiente
print(exp_3)



#TABELA
print(True and True)
print(True and False)
print(False and False)
print(True or True)
print(True or False)
print(False or False)


curso = "Curso de Python"
nome_curso = curso
saldo1, limite1 = 200, 200

curso is nome_curso #vai retornar "True"

curso is not nome_curso #vai retornar "False"

saldo1 is limite1 #vai retornar "True"


saldo = 1000
limite  = 500

print(saldo is limite) #False
print(saldo is not limite) #True

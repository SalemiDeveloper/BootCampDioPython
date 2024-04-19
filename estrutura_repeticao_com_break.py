while True: #estrutura de repetição com laço infinito
    numero = int(input("Informe um numero: "))

    if numero == 10:
        break

    print(numero)


for numero in range(10):
    if numero == 2:
        break
    print(numero, end=" ")

print() #quebra de linha

for numero in range(10):
    if numero == 2:
        continue
    print(numero, end=" ")


while True:
    numero = int(input("\nInforme um numero: "))

    if numero == 10:
        break

    if numero % 2 == 0:
        continue

    print(numero)

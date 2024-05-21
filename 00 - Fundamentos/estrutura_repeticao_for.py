texto = str(input("Insira um texto: "))
VOGAIS = "AEIOU"

#EXEMPLO UTILIZANDO UM ITERÁVEL
for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")

else:
    print("a") #adiciona uma quebra de linha
    print("Executa no final do laço.")



#EXEMPLO UTILIZANDO RANGE
for numero in range(0, 11):
    print(numero, end=" ")
#>>>0 1 2 3 4 5 6 7 8 9 10

print() #quebra de linha

#exibindo a tabuada do 5
for numero in range(0, 51, 5):
    print(numero, end=" ")
#>>> 0 5 10 15 20 25 30 35 40 45 50


"""
    PRIMEIRO PROGRAMA POO

    João tem uma biciletaria e gostaria de registrar as vendas de suas bicicletas.
    Crie um programa onde Jõa informe: cor, modelo, ano e valor da bicicleta vendida. 
    Uma bicicleta pode: buzinar, parar e correr. Adicione esses comportamentos!
"""

class Bicicleta:
    def __init__(self, cor, modelo, ano, valor):
        #self é parecido com o this em java
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

    
    def buzinar(self):
        print("Plim plim...")


    def parar(self):
        print("Parando bicielta...")
        print("Bicicleta parada!")


    def correr(self):
        print("Vrummmm...")


    #def __str__(self):
    #    return f"Bicicleta: cor = {self.cor}, modelo = {self.modelo}, ano = {self.ano}, valor = {self.valor}"
    

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"



b1 = Bicicleta("vermelha", "caloi", 2022, 600)
b1.buzinar()
b1.correr()
b1.parar()
#acessando os atributos
print(b1.cor, b1.modelo, b1.ano, b1.valor)

b2 = Bicicleta("verde", "monark", 2000, 189)
Bicicleta.buzinar(b2) #b2.buzinar() -> mesma coisa

print(b2)

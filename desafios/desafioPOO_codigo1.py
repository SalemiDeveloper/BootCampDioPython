# TODO: Crie uma classe UsuarioTelefone.
class UsuarioTelefone:
    # TODO: Defina um método especial `__init__`, que é o construtor da classe.
    # O método `__init__` irá inicializar os atributos da classe: `nome`, `numero` e `plano`.
    def __init__(self, nome, numero, plano):
        # TODO: Aplique o conceito de encapsulamento, onde os atributos serão encapsulados dentro da classe.
        self.__nome = nome
        self.__numero = numero
        self.__plano = plano

    # Método para acessar o nome
    def get_nome(self):
        return self.__nome

    # Método para acessar o número
    def get_numero(self):
        return self.__numero

    # Método para acessar o plano
    def get_plano(self):
        return self.__plano

    # Método para alterar o nome
    def set_nome(self, nome):
        self.__nome = nome

    # Método para alterar o número
    def set_numero(self, numero):
        self.__numero = numero

    # Método para alterar o plano
    def set_plano(self, plano):
        self.__plano = plano

    # A classe `UsuarioTelefone` define um método especial `__str__`, que retorna uma representação em string do objeto.
    def __str__(self):
        return f"Usuário {self.__nome} criado com sucesso."

# Entrada:
nome = input()
numero = input()
plano = input()

# TODO: Crie um novo objeto `UsuarioTelefone` com os dados fornecidos:
usuario = UsuarioTelefone(nome, numero, plano)

print(usuario)

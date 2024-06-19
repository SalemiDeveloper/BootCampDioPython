# Definição da classe PlanoTelefone
class PlanoTelefone:
    def __init__(self, nome, saldo):
        self.__nome = nome
        self.__saldo = saldo
    
    def get_nome(self):
        return self.__nome
    
    def get_saldo(self):
        return self.__saldo
    
    def verificar_saldo(self):
        saldo = self.__saldo
        
        if saldo < 10:
            mensagem = "Seu saldo está baixo. Recarregue e use os serviços do seu plano."
        elif saldo >= 50:
            mensagem = "Parabéns! Continue aproveitando seu plano sem preocupações."
        else:
            mensagem = "Seu saldo está razoável. Aproveite o uso moderado do seu plano."
        
        return saldo, mensagem

# Definição da classe UsuarioTelefone
class UsuarioTelefone:
    def __init__(self, nome, plano):
        self.__nome = nome
        self.__plano = plano
    
    def verificar_saldo(self):
        return self.__plano.verificar_saldo()
    
    def mensagem_personalizada(self):
        _, mensagem = self.verificar_saldo()
        return mensagem

# Recebendo as entradas do usuário (nome, plano, saldo):
nome_usuario = input()
nome_plano = input()
saldo_inicial = float(input())

# Criação de objetos do plano de telefone e usuário de telefone com dados fornecidos:
plano_usuario = PlanoTelefone(nome_plano, saldo_inicial)
usuario = UsuarioTelefone(nome_usuario, plano_usuario)

# Chamada do método para gerar mensagem personalizada com base no saldo:
mensagem = usuario.mensagem_personalizada()
print(mensagem)

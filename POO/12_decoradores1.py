def mensagem(nome):
    print("Executando mensagem")
    return f'Oi {nome}'

def mensagem_longa(nome):
    print('executando mensagem longa')
    return f'Olá {nome}, tudo bem com você?'

def executar(funcao, nome):
    print("Executando executar")
    return funcao(nome)


print(executar(mensagem, "Pedro"))
print(executar(mensagem_longa, "Pedro"))

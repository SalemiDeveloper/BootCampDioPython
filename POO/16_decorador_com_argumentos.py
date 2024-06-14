def meu_decorador(funcao):
    def envelope(*args, **kwargs):
        print("faz algo antes de executar")
        funcao(*args, **kwargs)
        print("faz algo depois de executar")

    return envelope

@meu_decorador
def ola_mundo(nome):
    print(f"Olá Mundo! {nome}")


#ola_mundo = meu_decorador(ola_mundo)
ola_mundo("Pedro")

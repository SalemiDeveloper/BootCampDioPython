def meu_decorador(funcao):
    def envelope(*args, **kwargs):
        print("faz algo antes de executar")
        resultado = funcao(*args, **kwargs)
        print("faz algo depois de executar")
        return resultado

    return envelope

@meu_decorador
def ola_mundo(nome):
    print(f"Olá Mundo! {nome}")
    return nome.upper()


#ola_mundo = meu_decorador(ola_mundo)
resultado = ola_mundo("Pedro")
print(resultado)

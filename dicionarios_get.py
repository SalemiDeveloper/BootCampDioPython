contatos = {"pedro@gmail.com":{ "nome": "Pedro", "telefone": "1111-1111"}}

#contatos["chave"] #KeyError

resultado = contatos.get("chave")
print(resultado)

resultado = contatos.get("chave", {})
print(resultado)

resultado = contatos.get(
    "pedro@gmail.com", {}
)
print(resultado)

contatos = {
    "pedro@gmail.com": {"nome" : "Pedro", "telefone": "1111-1111"}, 
    "joao@gmail.com": {"nome": "João", "telefone": "2222-2222"}, 
    "gustavo@gmail.com": {"nome": "Gustavo", "telefone": "3333-3333"}
}

resultado = "pedro@gmail.com" in contatos
print(resultado)

resultado = "aaaa@gmail.com" in contatos
print(resultado)

resultado = "telefone" in contatos["gustavo@gmail.com"]
print(resultado)

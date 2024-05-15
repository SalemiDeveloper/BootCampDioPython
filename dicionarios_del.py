contatos = {
    "pedro@gmail.com": {"nome" : "Pedro", "telefone": "1111-1111"}, 
    "joao@gmail.com": {"nome": "João", "telefone": "2222-2222"}, 
    "gustavo@gmail.com": {"nome": "Gustavo", "telefone": "3333-3333"}
}

#deleta só o telefone
del contatos["pedro@gmail.com"]["telefone"]

#deleta tudo da chave
del contatos["joao@gmail.com"]

#deleta todo o dicionário
del contatos

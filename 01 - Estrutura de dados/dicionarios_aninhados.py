contatos = {
    "pedro@gmail.com": {"nome" : "Pedro", "telefone": "1111-1111"}, 
    "joao@gmail.com": {"nome": "João", "telefone": "2222-2222"}, 
    "gustavo@gmail.com": {"nome": "Gustavo", "telefone": "3333-3333"}
}

telefone = contatos["joao@gmail.com"]["telefone"]
print(telefone)

for chave in contatos:
    print(chave, contatos[chave])

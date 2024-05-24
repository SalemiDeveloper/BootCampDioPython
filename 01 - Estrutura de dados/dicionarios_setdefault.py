contato = {"nome": "Pedro", "telefone": "1111-1111"}

contato.setdefault("nome", "João")
print(contato)

#vai inserir caso não exista
contato.setdefault("idade", 28)
print(contato)

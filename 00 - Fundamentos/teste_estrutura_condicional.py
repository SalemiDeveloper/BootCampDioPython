saldo = 2000.0
print(f"SALDO = {saldo}")
saque = float(input("Informe o valor que deseja sacar: "))
cheque_especial = 200

if saque > saldo:
    res = str(input("Saldo insuficiente, deseja usar cheque especial? s/n: "))

    if res == "s":
        if saque <= saldo + cheque_especial:
            print("Saque realizado com uso do cheque especial.")
        else:
            print("Saldo insuficiente.")
    else:
        print("Você não tem saldo suficiente e optou por não usar cheque especial. Programa encerrado.")

else:
    print("Saque realizado com sucesso.")
        

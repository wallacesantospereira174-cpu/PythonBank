contas = {}
def menu():
     print("||","=" * 30, "||")
     print("||       Banco Master         ||")
     print("||","=" * 30, "||")
     print("1 - Criar conta")
     print("2 - Depositar")
     print("3 - Sacar")
     print("4 - Transferir")
     print("5 - Consultar saldo")
     print("6 - Listar contas")
     print("7 - Excluir conta")
     print("0 - Sair")
     print("||","=" * 30, "||")

def pesquisa():
     while True:
         try:
              buscar = int(input("Digite um comando do menu:"))
              return buscar
         except ValueError:
              print("Comando não existente por favor digite um comando valido.")

def criar_conta():
     nome = input("Digite seu nome:")
     while True:
          try:
              cpf = int(input("Digite seu CPF:"))
              break
          except ValueError:
               print("Número não correspondente.")

     conta_cpf = (cpf,)
     contas[conta_cpf] = {
          "nome": nome,
          "saldo":0,
          "historico": [],
     }

def depositar():
     while True:
          try:
               numero_de_conta = int(input("Número da conta:"))
               break
          except ValueError:
               print("Comando não existente por favor digite um comando valido.")


     conta = (numero_de_conta,)

     if conta in contas:
            while True:
                    try:
                        valor = int(input("Valor a ser depositado:"))
                        break
                    except ValueError:
                         print("Valor invalido.")

            contas[conta]["saldo"] += valor

            contas[conta]["historico"].append(f'Deposito:R$ {valor}')

            print(f'\n Valor depositado com sucesso!')
     else:
          print("Conta não encontrada!" )    

def sacar():
    while True:
        try:
            numero_de_conta = int(input("Número da conta: "))
            break
        except ValueError:
            print("Comando não existente, por favor digite um comando válido.")

    conta = (numero_de_conta,)

    if conta in contas:
        saldo = contas[conta]["saldo"]
        if saldo > 0:
            print(f"Saldo atual: R$ {saldo:.2f}")

            while True:
                try:
                    valor_saque = float(input("Valor a ser sacado: "))
                    break
                except ValueError:
                    print("\nPor favor, digite um valor válido.")

            if valor_saque > 0:
                if saldo >= valor_saque:
                    contas[conta]["saldo"] -= valor_saque
                    saldo_atual = contas[conta]["saldo"]
                    print(f'Saldo atual: R$ {saldo_atual:.2f}')
                    contas[conta]["historico"].append(f'Saque: R$ {valor_saque:.2f}')
                else:
                    print("Saldo insuficiente.")
            else:
                print("O valor do saque deve ser maior que zero.")
        else:
            print("Saldo indisponível para realizar saques.")
    else:
        print("Conta não existe!")


while True:
     menu()
     consulta = pesquisa()
     
     if consulta == 1:
          criar_conta()
     elif consulta == 2:
          depositar()
     elif consulta == 3:
           sacar()
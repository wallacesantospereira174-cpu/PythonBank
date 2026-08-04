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
                        valor = float(input("Valor a ser depositado:"))
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

def transferir():
     def buscar_conta():
          while True:
               try:
                    conta_busca = int(input("Número de conta de usuario:"))
                    return conta_busca
               except ValueError:
                    print("Comando não existente, por favor digite um comando válido.")
     busca = buscar_conta()
     conta = (busca,)
     if conta in  contas:
          while True:
               try:
                    transferencia = float(input("Valor de transferência:"))
                    break
               except ValueError:
                    print("Coloque um valor valido.")
                    
          saldo = contas[conta]["saldo"]
          if transferencia > 0:
               if saldo >= transferencia:
                    chave_de_conta_receptora =  buscar_conta()
                    conta_recebe = (chave_de_conta_receptora,)
                    if conta_recebe in contas:
                         if conta_recebe == conta:
                              print("Não pode fazer uma trazação para você mesmo.")  
                         else:
                              nome_cliente1 = contas[conta]["nome"]
                              nome_cliente2 = contas[conta_recebe]["nome"]
                              contas[conta]["historico"].append(f'Transferência de R$ {transferencia:.2f} para {nome_cliente2}')
                              contas[conta]["saldo"] -= transferencia
                              contas[conta_recebe]["saldo"] += transferencia
                              contas[conta_recebe]["historico"].append(f'Recebido de {nome_cliente1} R$: {transferencia:.2f} ')  
                         
                    else:
                         print("Conta não encontrada.")
                         
               else:
                    print("Saldo insuficiente.")
          else:
               print("Valor tem que ser maior que zero.")
     else:
          print("Conta não existente.")
          
def Consultar_saldo():
     def buscar_conta():
          while True:
               try:
                    conta_busca = int(input("Número de conta de usuario:"))
                    return conta_busca
               except ValueError:
                    print("Comando não existente, por favor digite um comando válido.")
     busca = buscar_conta()
     conta = (busca,)
     if conta in contas:
          if not contas[conta]["historico"]:
               print("Histórico vazio.")
          else:
               print("||" + "="*30 +  "||")
               print("||"   +   " Historico "  +    "||")
               saldo = contas[conta]["saldo"]
               for  historico in contas[conta]["historico"]:
                    print(historico)
               
               print("||"  + "="*30  + "||")
               print("||"  +   "Saldo disponivel "  +   "||")
               print("="*30)
               print(f"Saldo disponivel R$: {saldo:.2f}")
          
               print("||" +  "="*30 +  "||")
     else:
          print("Conta não existente.")
          

def Listar_contas():
     if not contas:
          print("Não existe nenhuma conta cadastrada.")
     else:
          print("=" * 35)
          print("      CONTAS CADASTRADAS")
          print("=" * 35)
          for cpf, dados in contas.items():
               print(f"CPF: {cpf[0]}")
               print(f"Nome: {dados['nome']}")
               print(f"Saldo: R$ {dados['saldo']:.2f}")
               print("-" * 30)
          print("=" * 35)

def excluir_conta():
     def buscar_conta():
          while True:
               try:
                    conta_busca = int(input("Número de conta de usuario:"))
                    return conta_busca
               except ValueError:
                    print("Comando não existente, por favor digite um comando válido.")
     busca = buscar_conta()
     conta = (busca,)
     if conta in contas:
          nome_conta = contas[conta]["nome"]
          print("="*30)
          print(f"Deseja mesmo excluir conta: {nome_conta}?")
          print(" Digite 'sim' para confirmar ou 'não' para cancelar.")
          while True:
               opcao = input("Digite Sim ou Não:").strip().lower()
               if opcao == "sim":
                    print(f"A conta de {nome_conta} foi excluída com sucesso.")
                    contas.pop(conta)
                    break
               elif opcao == "não" or opcao == "nao":
                    print(f"Conta {nome_conta} cancelada a exclusão. ")
                    break
               else:
                    print("Digite Sim ou Não para confirmar.")
     else:
          print("Conta não cadastrada ")

while True:
     menu()
     consulta = pesquisa()
     
     if consulta == 1: 
          criar_conta()
     elif consulta == 2:
          depositar()
     elif consulta == 3:
          sacar()
     elif consulta == 4:
          transferir()
     elif consulta == 5:
          Consultar_saldo()
     elif consulta == 6:
          Listar_contas()     
     elif consulta == 7:
          excluir_conta()
     elif consulta == 0:
          print("Fechando banco Master.")
          break

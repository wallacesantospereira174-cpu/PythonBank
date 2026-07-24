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


while True:
     menu()
     consulta = pesquisa()
     
     if consulta == 1:
          criar_conta()
     elif consulta == 2:
          
          
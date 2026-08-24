contas = {}

def menu():
    print("||", "=" * 30, "||")
    print("          Banco Master         ")
    print("||", "=" * 30, "||")
    print("          1 - Criar conta")
    print("          2 - Depositar")
    print("          3 - Sacar")
    print("          4 - Transferir")
    print("          5 - Consultar saldo")
    print("          6 - Listar contas")
    print("          7 - Excluir conta")
    print("          0 - Sair")
    print("||", "=" * 30, "||")

def pesquisa_conta():
    while True:
        try:
            cpf = int(input("Digite o numero da conta (CPF): "))    
            return cpf
        except ValueError:
            print("Número de conta inválido.")

class Conta:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf 
        self.saldo = 0.0
        self.historico = []

    def depositar(self, valor):
        if valor <= 0:
            print("Valor inválido.")
            return
        self.saldo += valor
        self.historico.append(f"Depósito R$: {valor:.2f}")
        print("Depósito realizado com sucesso!")

    def Sacar(self, sacar_valor):
        if sacar_valor <= 0:
            print("Valor de saque inválido.")
            return False
            
        if self.saldo >= sacar_valor:
            self.saldo -= sacar_valor
            self.historico.append(f"Saque R$: {sacar_valor:.2f}")
            print("Saque realizado com sucesso!")
            return True
        else:
            print("Saldo insuficiente.")
            return False

    def transferir(self, valor, conta_receptora):
        if valor <= 0:
            print("Valor inválido.")
            return
            
        if self.Sacar(valor):
            conta_receptora.depositar(valor)
            self.historico.append(f"Transferência enviada para {conta_receptora.nome} R$: {valor:.2f}")
            conta_receptora.historico.append(f"Transferência recebida de {self.nome} R$: {valor:.2f}")
            print("Transferência concluída com sucesso!")

class ContaCorrente(Conta):
    def __init__(self, nome, cpf, limite=500.0, taxa_saque=2.50):
        super().__init__(nome, cpf)
        self.limite = limite
        self.taxa_saque = taxa_saque

    def Sacar(self, sacar_valor):
        if sacar_valor <= 0:
            print("Valor de saque inválido.")
            return False
            
        valor_total = sacar_valor + self.taxa_saque
        
        if (self.saldo + self.limite) >= valor_total:
            self.saldo -= valor_total
            self.historico.append(f"Saque C.Corrente R$: {sacar_valor:.2f} (Taxa: R$ {self.taxa_saque:.2f})")
            print(f"Saque realizado! Taxa de R$ {self.taxa_saque:.2f} aplicada.")
            return True
        else:
            print(f"Saldo + Limite insuficiente. Disponível total: R$ {(self.saldo + self.limite):.2f}")
            return False

def cria_conta(nome, cpf, tipo_conta):
    if tipo_conta == 2:
        limite = float(input("Digite o limite do cheque especial (Ex: 500): R$ "))
        return ContaCorrente(nome, cpf, limite)
    else:
        return Conta(nome, cpf)

def verifica_conta():
    cpf = pesquisa_conta()
    if cpf in contas:
        conta = contas[cpf]           
        valor = float(input("Digite o valor a ser depositado: R$ "))
        conta.depositar(valor)
        print(f"Novo Saldo: R$ {conta.saldo:.2f}")
    else:
        print("Conta não cadastrada.")

def saque():
    cpf = pesquisa_conta()
    if cpf in contas:
        conta = contas[cpf]
        sacar_valor = float(input("Digite o valor do saque: R$ "))
        conta.Sacar(sacar_valor)
    else:
        print("Conta não existe.")   

def transferebcia():
    cpf = pesquisa_conta()
    if cpf in contas:
        conta = contas[cpf]
        while True:
            try:
                valor = float(input("Digite o valor da transferência: R$ "))
                break
            except ValueError:
                print("Valor inválido.")
        
        conta2 = pesquisa_conta()
        if conta2 in contas:
            if conta2 == cpf:
                print("Não é possível transferir para a mesma conta.")
            else:
                conta_receptora = contas[conta2]
                conta.transferir(valor, conta_receptora)
        else:
            print("Conta de destino não existe.")
    else:
        print("Conta de origem não existe.")

def Consultar_saldo():
    cpf = pesquisa_conta()
    if cpf in contas:
        cont = contas[cpf]
        print("=" * 35)
        print(f"Titular: {cont.nome}")
        print(f"Tipo: {'Conta Corrente' if isinstance(cont, ContaCorrente) else 'Conta Comum'}")
        print("=" * 35)
        print(f"Saldo atual: R$ {cont.saldo:.2f}")
        
        if isinstance(cont, ContaCorrente):
            print(f"Limite Cheque Especial: R$ {cont.limite:.2f}")
            print(f"Total Disponível: R$ {(cont.saldo + cont.limite):.2f}")
            
        print("-" * 35)
        print("HISTÓRICO DE TRANSAÇÕES:")
        if not cont.historico:
            print("Nenhuma transação realizada.")
        else:
            for item in cont.historico:
                print(f"- {item}")
        print("=" * 35)
    else:
        print("Conta não existente.")

def listar_contas():
    if not contas:
        print("Nenhuma conta cadastrada.")
        return

    print("=" * 35)
    print("       CONTAS CADASTRADAS        ")
    print("=" * 35)
    for cpf, conta in contas.items():
        tipo = "Conta Corrente" if isinstance(conta, ContaCorrente) else "Conta Comum"
        print(f'Nome: {conta.nome}')
        print(f'CPF: {cpf}')
        print(f'Tipo: {tipo}')
        print(f'Saldo: R$ {conta.saldo:.2f}')
        print("=" * 35) 

def Excluir_conta():
    cpf = pesquisa_conta()
    if cpf in contas:
        contas.pop(cpf)
        print("=" * 30)
        print("Conta excluída com sucesso.")
        print("=" * 30)
    else:
        print("Conta não está cadastrada.")

while True:
    menu()
    try:
        opcao = int(input("Digite uma opção do menu: "))
    except ValueError:
        print("Opção inválida!")
        continue

    if opcao == 1:
        nome = input("Digite seu nome: ")
        cpf = int(input("Digite seu CPF: "))
        print("\nEscolha o tipo de conta:")
        print("1 - Conta Comum")
        print("2 - Conta Corrente (com Limite e Taxa de Saque)")
        tipo = int(input("Opção: "))
        
        conta = cria_conta(nome, cpf, tipo)
        contas[cpf] = conta
        print("Conta criada com sucesso!")

    elif opcao == 2:
        verifica_conta()
    elif opcao == 3:
        saque()
    elif opcao == 4:
        transferebcia()
    elif opcao == 5:
        Consultar_saldo()
    elif opcao == 6:
        listar_contas()
    elif opcao == 7:
        Excluir_conta()
    elif opcao == 0:
        print("Sistema fechado.")
        break
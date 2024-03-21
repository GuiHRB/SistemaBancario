def menu():

    print(f""" 
    =============== MENU ===============

    [1]\tDepositar
    [2]\tSacar                          
    [3]\tExtrato
    [4]\tNovo Usuário
    [5]\tNova Conta
    [6]\tListar Contas

    [0]\tSair  
    """)
    return input("=> ")
    
def criar_usuario(lista, len):
    payload = {}
    dados = ("nome", "data de nascimento", "cpf", "endereço")
    for dado in dados:
        payload[dado] = input(f"Digite {dado}: ")
    if len > 0:
        for dado in range(0,len):
            if payload["cpf"] in lista[dado]["cpf"]:
                print(f"Cpf informado já vinculado em outro usuário!")
                break
            elif dado == len - 1:
                lista.append(payload)
                print(f"Usuário cadastrado com sucesso!")
    else:
        lista.append(payload)
        print(f"Usuário cadastrado com sucesso!")

def listar_conta(contas):
    for conta in contas:
        print(f"""
    ##################################### 
                
    Agência:\t{conta["agência"]}
    C/C:\t\t{conta["número_conta"]}
    Titular:\t{conta["usuário"]["nome"]}
            """)

def criar_conta(lista,user,len_user,len_lista):

    payload = {"agência":"0001"}
    cpf = input(f"Digite o cpf que você quer vincular essa conta: ")
    if len_user > 0:
        for dado in range(0,len_user):
            if cpf in user[dado]["cpf"]:
                payload["número_conta"] = str(len_lista+1)
                payload["usuário"] = user[dado]
                lista.append(payload)
                print(f"Conta criada!")
                break
            elif dado == len_user - 1:
                print(f"Usuário não encontrado!")
    else:
        print(f"Não há usuários cadastrados!")

def saque(*,saldo,extrato,saques,l_saque,l_saques):
    saque = float(input("Digite o valor do saque: "))
    if saques < l_saques:
            if saque <= 0:
                print("Não é possível sacar esse valor!")
            elif saque > l_saque:
                print("Limite de R$ 500.00 por saque!")
            elif saque > saldo:
                print("Saldo Insuficiente")
            else: 
                saldo -= saque
                extrato += f"""
        Saque de R$ {saque:.2f}
    """
                saques += 1
    else:  
        print("Limite de saques diários atingido!")
    return saldo,extrato,saques

def deposito(saldo,extrato,/):
    deposito = float(input("Digite o valor do depósito: "))
    if deposito <= 0:
        print("Não é possível depositar esse valor!")
        
    else:
        saldo += deposito
        extrato += f"""
        Depósito de R$ {deposito:.2f}
    """
    return saldo,extrato

def ver_extrato(saldo,extrato):
    print(f"""
    #########      EXTRATO     #########

    {extrato}
    
    Saldo atual da conta : R$ {saldo:.2f}

    #################################### """
    )

saldo = 0
saques = 0 
extrato = ""
LIMITE_SAQUES = 3
LIMITE_SAQUE = 500
usuario = []
conta_corrente = []

while True:

    choice = menu()

    if choice == "1" :
        saldo,extrato = deposito(saldo,extrato)
        
    elif choice == "2":
        saldo,extrato,saques = saque(saldo=saldo,extrato=extrato,saques=saques,l_saque=LIMITE_SAQUE,l_saques=LIMITE_SAQUES)
        
    elif choice == "3":
        ver_extrato(saldo,extrato)

    elif choice == "4":
        criar_usuario(usuario,len(usuario))

    elif choice == "5":
        criar_conta(conta_corrente,usuario,len(usuario),len(conta_corrente))
    
    elif choice == "6":
        listar_conta(conta_corrente)

    elif choice == "0":
        break

    else:
        print("Opção Inválida")    

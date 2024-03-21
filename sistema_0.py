saldo = 5000
saques = 0 
extrato = ""

while True:

    print(f""" 
######## BANCO ########

    [1] - Depósito
    [2] - Saque                             
    [3] - Extrato

    [0] - Sair    
          
#######################          
""")
    choice = int(input("Selecione uma opção: "))

    if choice == 1 :
        deposito = float(input("Digite o valor do depósito: "))
        if deposito <= 0:
            print("Não é possível depositar esse valor!")
        else:
            saldo += deposito
            extrato += f"Depósito de R$ {deposito:.2f}\n"

    elif choice == 2:
        saque = float(input("Digite o valor do saque: "))
        if saques <3:
            if saque <= 0:
                print("Não é possível sacar esse valor!")
            elif saque >500:
                print("Limite de R$ 500.00 por saque!")
            elif saque > saldo:
                print("Saldo Insuficiente")
            else: 
                saldo -= saque
                extrato += f"Saque de R$ {saque:.2f}\n"
                saques += 1
        else:
            print("Limite de saques diários atingido!")

    elif choice == 3:
        print(f"{extrato}Saldo atual da conta : R$ {saldo:.2f} ")

    elif choice == 0:
        break

    else:
        print("Opção Inválida")    

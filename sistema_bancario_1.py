from abc import ABC, abstractclassmethod, abstractproperty

class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []
    
    def adicionar_conta(self, conta):
        self.contas.append(conta)

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)
    
class PessoaFisica(Cliente):
    def __init__(self, nome, cpf, data_nascimento, endereco):
        super().__init__(endereco)
        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = data_nascimento
   
class Conta:
    def __init__(self, numero, cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()

    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)
    
    @property
    def saldo(self):
        return self._saldo
    
    @property
    def numero(self):
        return self._numero
    
    @property
    def agencia(self):
        return self._agencia
    
    @property
    def cliente(self):
        return self._cliente
    
    @property
    def historico(self):
        return self._historico
    
    def sacar(self, valor):
        saldo = self.saldo

        if valor > saldo:
            print("Saldo Insuficiente")
        
        elif valor <= 0:
            print("Não é possível sacar esse valor!")
        
        else:
            self._saldo -= valor
            print("Saque realizado com sucesso!")
            return True

        return False

    def depositar(self, valor):
        if valor <= 0:
            print("Não é possível depositar esse valor!")
        
        else:
            self._saldo += valor
            print("Depósito realizado com sucesso!")
            return True
        
        return False

class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        super().__init__(numero, cliente)
        self.limite = limite
        self.limite_saques = limite_saques

    def sacar(self, valor):
        numero_saques = len(
            [transacao for transacao in self.historico.transacoes if transacao["tipo"] == Saque.__name__]
        )

        if valor > self.limite:
            print("Valor excedeu o limite de saque!")
        
        elif numero_saques >= self.limite_saques:
            print("Limite de Saques atingindo!")
        
        else:
            return super().sacar(valor)
        
        return False
    
    def __str__(self):
        return f"""
Agência:\t{self.agencia}
C/C:\t\t{self.numero}
Titular:\t{self.cliente.nome}
        """

class Historico:
    def __init__(self):
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes
    
    def adicionar_transacao(self, transacao):
        self._transacoes.append(
            {
                
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor
            }
        )

class Transacao(ABC):
    @property
    @abstractproperty
    def valor(self):
        pass

    @abstractclassmethod
    def registrar(self, conta):
        pass

class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor
    
    @property
    def valor(self):
        return self._valor
    
    def registrar(self, conta):
        sucesso_transacao = conta.sacar(self.valor)
        
        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)

class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor
    
    def registrar(self, conta):
        sucesso_transaco = conta.depositar(self.valor)

        if sucesso_transaco:
            conta.historico.adicionar_transacao(self)

def filtrar_cliente(cpf, clientes):
    for cliente in clientes:
        if cliente.cpf == cpf:
            return cliente
    return None

def criar_cliente(clientes):
    cpf = input("Digite seu cpf (Apenas números): ")
    cliente = filtrar_cliente(cpf, clientes)

    if cliente:
        print("Cpf já cadastrado em outro cliente!")
        return
    
    nome = input("Digite seu nome completo: ")
    data = input("Data de nascimento (dd/mm/yy): ")
    endereco = input("Endereço (logradouro,nro - bairro - cidade/sigla estado): ")

    clientes.append(PessoaFisica(nome,cpf,data,endereco))
    print("Cliente criado com sucesso!")

def criar_conta(clientes, contas):
    cpf = input("Digite seu cpf (Apenas números): ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("Cliente não localizado!")
        return
    
    numero = len(contas) + 1
    conta = ContaCorrente.nova_conta(cliente, numero)
    contas.append(conta)
    cliente.adicionar_conta(conta)

    print("Conta criada!")

def listar_contas(contas):
    for conta in contas:
        print(conta)

def recuperar_conta(clientes):
    cpf = input("Digite o cpf: ")
    cliente = filtrar_cliente(cpf,clientes)
    
    if cliente:
        if len(cliente.contas) > 0:
            return cliente.contas[0]
        print("Esse cliente não possui contas!")
        return None
    
    print("Cliente não localizado!")
    return None

def sacar(clientes):
    conta = recuperar_conta(clientes)
    
    if conta:
        valor = float(input("Digite o valor de saque: "))
        Saque(valor).registrar(conta)

def depositar(clientes):
    conta = recuperar_conta(clientes)

    if conta:
        valor = float(input("Digite o valor de depósito: "))
        Deposito(valor).registrar(conta)

def extrato(clientes):
    conta = recuperar_conta(clientes)

    if conta:
        extratos = conta.historico.transacoes
        for extrato in extratos:
            print(f"""Tipo: {extrato["tipo"]}
Valor: R${extrato["valor"]:.2f}
""")

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

def main():
    clientes = []
    contas = []
    
    while True:

        choice = menu()

        if choice == "1" :
            print(f"======== Depósito ========")
            depositar(clientes)
            
        elif choice == "2":
            print(f"========= Saque =========")
            sacar(clientes)
            
        elif choice == "3":
            print(f"======== Extrato ========")
            extrato(clientes)

        elif choice == "4":
            print(f"===== Novo Cliente =====")
            criar_cliente(clientes)

        elif choice == "5":
            print(f"====== Nova Conta ======")
            criar_conta(clientes, contas)

        elif choice == "6":
            print(f"======== Contas ========")
            listar_contas(contas)

        elif choice == "0":
            break

        else:
            print("Opção Inválida") 

main()
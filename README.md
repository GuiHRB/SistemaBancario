# ***Sistema Bancário***
Desenvolver um script de um sistema bancário de acesso único, que permite o usuário sacar, depositar e conferir seu extrato.

- *Cuidado com os depósitos e saques inválidos.*
- *Limite de 3 saques diários de no máximo R$ 500.00 cada saque.*
- *O extrato deve apresentar os depósitos e saques realizados e no final o saldo atual da conta.*
- *Valores no extrato no formato R$ xxx.xx*
- *Separar as funções existentes de saque, depósito e extrato em funções.*
- *Criar duas novas funções : cadastrar usuário (cliente) e cadastrar conta bancária.*
- *saque - keywords only.*
- *depósito - positional only.*
- *extrato - kwords and positional.*
- *Usuário - armazenar numa lista : nome / data de nascimento / cpf / endereco(string com formato: logadouro,nro - bairro - cidade/sigla estado). Cpf apenas números e único.*
- *Conta corrente - armazenar em uma lista : agencia, numero da conta e usuario. O numero da conta é sequencial, iniciando em 1. A agencia é fixa : 0001. O usuario pode ter mais de uma conta, mas a conta pertence a somente um usuario.*

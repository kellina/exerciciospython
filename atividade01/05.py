#-----------DICIONÁRIO-----------------
# Questão 01 - Escreva um programa que permita gerenciar o banco de dados de
# clientes de uma empresa. Os clientes serão salvos em um dicionário no qual a chave de
# cada cliente será seu CPF, e o valor será outro dicionário com os dados do cliente
# (nome, endereço, telefone, email, preferencial), onde preferencial terá o valor True se
# for de um cliente especial. O programa deve solicitar ao usuário uma opção no seguinte
# menu: (1) Adicionar cliente, (2) Remover cliente, (3) Mostrar cliente, (4) Listar todos
# os clientes, (5) Listar clientes preferenciais, (6) Terminar. Dependendo da opção
# escolhida, o programa deverá fazer o seguinte:
# Peça dados do cliente, crie um dicionário com os dados e adicione-o ao banco de dados.
# Peça o CPF do cliente e exclua seus dados do banco de dados.
# Peça o CPF do cliente e mostre seus dados.
# Mostrar lista de todos os clientes no banco de dados com seu CPF e nome.
# Mostre a lista de clientes preferenciais no banco de dados com seu CPF e nome.
# Termine o programa.

def adicionar_cliente(clientes):
  cpf = input("CPF: ")
  clientes[cpf] = {}
  clientes[cpf]["nome"] = input("Nome: ")
  clientes[cpf]["endereco"] = input("Endereço: ")
  clientes[cpf]["telefone"] = input("Telefone: ")
  clientes[cpf]["email"] = input("E-mail: ")
  clientes[cpf]["preferencial"] = input("Preferencial? [S/N]: ").upper() == "S"

def remover_cliente(clientes):
  cpf = input("CPF: ")
  if clientes.get(cpf) != None:
    del clientes[cpf]
    print(f"Cliente {cpf} removido.")
  else:
    print(f"Cliente {cpf} não encontrado.")
  input("Pressione <ENTER> para continuar...")
  

def mostrar_cliente(clientes):
  cpf = input("CPF: ")
  cliente = clientes.get(cpf)
  print("-------------------------------------------------")
  print(f"DADOS DO CLIENTE {cpf}")
  print("-------------------------------------------------")
  if cliente != None:
    print(f"Nome: {cliente['nome']}")
    print(f"Endereço: {cliente['endereco']}")
    print(f"Telefone: {cliente['telefone']}")
    print(f"E-mail: {cliente['email']}")
    print(f"Preferêncial: {cliente['preferencial']}")
  else:
    print(f"Cliente {cpf} não encontrado.")
  print("-------------------------------------------------")
  input("Pressione <ENTER> para continuar...")

def mostrar_clientes(clientes):
  print("-------------------------------------------------")
  print("LISTA DE CLIENTES")
  for cpf, cliente in clientes.items():
    print("-------------------------------------------------")
    print(f"CPF: {cpf}")
    print(f"Nome: {cliente['nome']}")
    print(f"Endereço: {cliente['endereco']}")
    print(f"Telefone: {cliente['telefone']}")
    print(f"E-mail: {cliente['email']}")
    print(f"Preferêncial: {cliente['preferencial']}")
    print("-------------------------------------------------")
  input("Pressione <ENTER> para continuar...")

def mostrar_clientes_preferenciais(clientes):
  print("-------------------------------------------------")
  print("LISTA DE CLIENTES PREFERENCIAIS")
  for cpf, cliente in clientes.items():
    if(cliente["preferencial"]):
      print("-------------------------------------------------")
      print(f"CPF: {cpf}")
      print(f"Nome: {cliente['nome']}")
      print(f"Endereço: {cliente['endereco']}")
      print(f"Telefone: {cliente['telefone']}")
      print(f"E-mail: {cliente['email']}")
      print(f"Preferêncial: {cliente['preferencial']}")
      print("-------------------------------------------------")
      input("Pressione <ENTER> para continuar...")

if __name__ == "__main__":
  clientes = {}

  while True:
    print("                     MENU                     ")
    print("----------------------------------------------")
    print("(1) Adicionar cliente")
    print("(2) Remover cliente")
    print("(3) Mostrar cliente")
    print("(4) Listar clientes")
    print("(5) Listar clientes preferenciais")
    print("(6) Terminar")

    opcao = int(input("Escolhar uma opção [1,2,3,4,5,6]: "))
    if opcao == 1:
      adicionar_cliente(clientes)
    elif opcao == 2:
      remover_cliente(clientes)
    elif opcao == 3:
      mostrar_cliente(clientes)
    elif opcao == 4:
      mostrar_clientes(clientes)
    elif opcao == 5:
      mostrar_clientes_preferenciais(clientes)
    elif opcao == 6:
      break

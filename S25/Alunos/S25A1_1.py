'''
Exibição do estoque inicial antes de qualquer operação
Um menu interativo que permite ao usuário:
- Vender produtos
- Adicionar ao estoque
- Exibir o estoque atual
- Sair do sistema
'''
# Estoque inicial
estoque = [20, 15, 10, 30, 5]

# Função para vender produtos
def vender_produto(estoque, produto, quantidade):
    if 0 <= produto < len(estoque):
        if estoque[produto] >= quantidade:
            estoque[produto] -= quantidade
            print(f"Venda realizada: {quantidade} unidades do Produto {produto + 1}")
        else:
            print("Estoque insuficiente para essa venda.")
    else:
        print("Produto inválido.")

# Função para adicionar produtos ao estoque
def adicionar_estoque(estoque, produto, quantidade):
    if 0 <= produto < len(estoque):
        estoque[produto] += quantidade
        print(f"{quantidade} unidades adicionadas ao Produto {produto + 1}")
    else:
        print("Produto inválido.")

# Função para exibir o estoque
def exibir_estoque(estoque):
    print("\n📦 Estoque Atual:")
    for i, quantidade in enumerate(estoque):
        print(f"Produto {i + 1}: {quantidade} unidades")
    print()

# Exibe o estoque inicial
print("📌 Estoque Inicial:")
exibir_estoque(estoque)

# Atualizações iniciais conforme o procedimento experimental
vender_produto(estoque, 0, 3)   # Produto 1
vender_produto(estoque, 3, 2)   # Produto 4
adicionar_estoque(estoque, 4, 10)  # Produto 5

# Exibe o estoque após atualizações iniciais
print("📌 Estoque após atualizações iniciais:")
exibir_estoque(estoque)

# Menu interativo
while True:
    print("📋 Menu de Operações:")
    print("1 - Vender produto")
    print("2 - Adicionar ao estoque")
    print("3 - Exibir estoque")
    print("4 - Sair")
    
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        try:
            produto = int(input("Digite o número do produto (1 a 5): ")) - 1
            quantidade = int(input("Quantidade a vender: "))
            vender_produto(estoque, produto, quantidade)
        except ValueError:
            print("Entrada inválida. Use apenas números inteiros.")
    elif opcao == "2":
        try:
            produto = int(input("Digite o número do produto (1 a 5): ")) - 1
            quantidade = int(input("Quantidade a adicionar: "))
            adicionar_estoque(estoque, produto, quantidade)
        except ValueError:
            print("Entrada inválida. Use apenas números inteiros.")
    elif opcao == "3":
        exibir_estoque(estoque)
    elif opcao == "4":
        print("Encerrando o sistema. Até logo!")
        break
    else:
        print("Opção inválida. Tente novamente.")


import json
import os

# 🔧 Configurações iniciais
ARQUIVO_ESTOQUE = "estoque.json"
NOMES_PRODUTOS = ["Arroz", "Feijão", "Macarrão", "Sabão", "Detergente"]
ESTOQUE_INICIAL = [20, 15, 10, 30, 5]
VENDAS_INICIAL = [0, 0, 0, 0, 0]

# 🧹 Limpa o terminal
def limpar_terminal():
    os.system("cls" if os.name == "nt" else "clear")

# 📥 Carrega os dados do arquivo ou inicia com valores padrão
def carregar_dados():
    if os.path.exists(ARQUIVO_ESTOQUE):
        with open(ARQUIVO_ESTOQUE, "r") as arquivo:
            dados = json.load(arquivo)
            if isinstance(dados, dict) and "estoque" in dados and "vendas" in dados:
                return dados["estoque"], dados["vendas"]
    return ESTOQUE_INICIAL.copy(), VENDAS_INICIAL.copy()

# 💾 Salva os dados no arquivo
def salvar_dados(estoque, vendas):
    with open(ARQUIVO_ESTOQUE, "w") as arquivo:
        json.dump({"estoque": estoque, "vendas": vendas}, arquivo)

# 📦 Exibe o estoque atual
def exibir_estoque(estoque):
    limpar_terminal()
    print("\n📦 ESTOQUE ATUAL")
    for i, quantidade in enumerate(estoque):
        print(f"{i + 1} - {NOMES_PRODUTOS[i]}: {quantidade} unidades")
    input("\nPressione Enter para voltar ao menu...")

# 🛍️ Registrar venda
def registrar_venda(estoque, vendas):
    limpar_terminal()
    print("\n🛍️ REGISTRAR VENDA")
    print("Digite 0 para voltar ao menu.")
    try:
        produto = int(input("Número do produto (1 a 5): "))
        if produto == 0:
            return
        quantidade = int(input("Quantidade vendida: "))
        if 1 <= produto <= 5:
            nome = NOMES_PRODUTOS[produto - 1]
            if estoque[produto - 1] >= quantidade:
                estoque[produto - 1] -= quantidade
                vendas[produto - 1] += quantidade
                print(f"✅ Você vendeu {quantidade} unidades de {nome}.")
            else:
                print(f"❌ Estoque insuficiente de {nome}!")
        else:
            print("❌ Produto inválido!")
    except ValueError:
        print("❌ Entrada inválida!")
    input("\nPressione Enter para voltar ao menu...")

# ➕ Adicionar ao estoque
def adicionar_estoque(estoque):
    limpar_terminal()
    print("\n➕ ADICIONAR AO ESTOQUE")
    print("Digite 0 para voltar ao menu.")
    try:
        produto = int(input("Número do produto (1 a 5): "))
        if produto == 0:
            return
        quantidade = int(input("Quantidade a adicionar: "))
        if 1 <= produto <= 5:
            nome = NOMES_PRODUTOS[produto - 1]
            estoque[produto - 1] += quantidade
            print(f"✅ Adicionadas {quantidade} unidades de {nome} ao estoque.")
        else:
            print("❌ Produto inválido!")
    except ValueError:
        print("❌ Entrada inválida!")
    input("\nPressione Enter para voltar ao menu...")

# 🧭 Menu principal
def menu_principal():
    estoque, vendas = carregar_dados()
    while True:
        limpar_terminal()
        print("\n🛒 MENU PRINCIPAL")
        print("1 - Exibir estoque")
        print("2 - Registrar venda")
        print("3 - Adicionar ao estoque")
        print("4 - Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            exibir_estoque(estoque)
        elif escolha == "2":
            registrar_venda(estoque, vendas)
            salvar_dados(estoque, vendas)
        elif escolha == "3":
            adicionar_estoque(estoque)
            salvar_dados(estoque, vendas)
        elif escolha == "4":
            print("👋 Saindo do sistema. Até logo!")
            break
        else:
            print("❌ Opção inválida!")
            input("\nPressione Enter para tentar novamente...")

# ▶️ Executa o programa
menu_principal()

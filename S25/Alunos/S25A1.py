'''
- Representação do estoque: usamos uma lista (vetor) com 5 posições, onde cada índice representa um tipo de produto.
- Funções criadas:
- vender_produto: subtrai a quantidade vendida do estoque.
- adicionar_estoque: adiciona unidades ao estoque.
- exibir_estoque: imprime o estoque atual.
- Execução das operações:
- Vendemos 3 unidades do produto 1 (índice 0).
- Vendemos 2 unidades do produto 4 (índice 3).
- Adicionamos 10 unidades ao produto 5 (índice 4).
- Exibimos o estoque final.

'''

# Código Python
# Estoque inicial
estoque = [20, 15, 10, 30, 5]

# Função para vender produtos
def vender_produto(estoque, produto, quantidade):
    if 0 <= produto < len(estoque):
        if estoque[produto] >= quantidade:
            estoque[produto] -= quantidade
        else:
            print(f"Estoque insuficiente para o produto {produto + 1}")
    else:
        print("Produto inválido")

# Função para adicionar produtos ao estoque
def adicionar_estoque(estoque, produto, quantidade):
    if 0 <= produto < len(estoque):
        estoque[produto] += quantidade
    else:
        print("Produto inválido")

# Função para exibir o estoque
def exibir_estoque(estoque):
    print("Estoque atual:")
    for i, quantidade in enumerate(estoque):
        print(f"Produto {i + 1}: {quantidade} unidades")

# Procedimento experimental
vender_produto(estoque, 0, 3)   # Produto 1
vender_produto(estoque, 3, 2)   # Produto 4
adicionar_estoque(estoque, 4, 10)  # Produto 5
exibir_estoque(estoque)

'''
Resultado esperado
Após executar o código, o estoque atualizado será:
Produto 1: 17 unidades
Produto 2: 15 unidades
Produto 3: 10 unidades
Produto 4: 28 unidades
Produto 5: 15 unidades
'''
# LLP-S26A1-Registro
'''
Leia um valor e faça um programa que coloque o valor lido na primeira posição de um vetor N[10].
Em cada posição subsequente, coloque o dobro do valor da posição anterior. 

Por exemplo, se o valor lido for 1, os valores do vetor deverão ser 1, 2, 4, 8, 
e assim sucessivamente. Mostre o vetor em seguida.

Entrada:
A entrada contém um valor inteiro (V<=50).

Saída:
Para cada posição do vetor, escreva "N[i] = X", em que 
    i é a posição do vetor e X é o valor armazenado na posição i. 
    O primeiro número do vetor N (N[0]) vai receber o valor de V.
    
'''
# Lê o valor inteiro V
V = int(input())

# Inicializa o vetor N com 10 posições
N = [0] * 10

# Atribui o valor lido à primeira posição
N[0] = V

# Preenche as demais posições com o dobro da anterior
for i in range(1, 10):
    N[i] = N[i - 1] * 2

# Exibe o vetor conforme o formato solicitado
for i in range(10):
    print(f"N[{i}] = {N[i]}")

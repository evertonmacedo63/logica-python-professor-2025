import tkinter as tk
from tkinter import messagebox

def gerar_vetor_dobro(valor_inicial, tamanho=10):
    vetor = [valor_inicial]
    for _ in range(1, tamanho):
        vetor.append(vetor[-1] * 2)
    return vetor

def exibir_resultado():
    try:
        V = int(entrada_valor.get())
        if V < 0 or V > 50:
            raise ValueError("Valor fora do intervalo permitido (0 a 50).")
        vetor = gerar_vetor_dobro(V)
        resultado_texto = "\n".join([f"N[{i}] = {valor}" for i, valor in enumerate(vetor)])
        resultado_label.config(text=resultado_texto)
    except ValueError as e:
        messagebox.showerror("Erro", str(e))

# Janela principal
janela = tk.Tk()
janela.title("Gerador de Vetor Dobrado")
janela.geometry("300x400")

# Entrada de valor
tk.Label(janela, text="Digite um valor inteiro (até 50):").pack(pady=10)
entrada_valor = tk.Entry(janela)
entrada_valor.pack()

# Botão de gerar
tk.Button(janela, text="Gerar Vetor", command=exibir_resultado).pack(pady=10)

# Área de resultado
resultado_label = tk.Label(janela, text="", justify="left", font=("Courier", 10))
resultado_label.pack(pady=10)

# Inicia a interface
janela.mainloop()
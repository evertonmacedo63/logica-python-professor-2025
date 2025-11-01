import tkinter as tk
from tkinter import messagebox

def converter_para_binario_com_explicacao(numero):
    restos = []
    explicacao = []

    original = numero
    while numero > 0:
        quociente = numero // 2
        resto = numero % 2
        restos.append(resto)
        explicacao.append(f"{numero} ÷ 2 = {quociente} com resto {resto}")
        numero = quociente

    binario = ''.join(str(bit) for bit in reversed(restos)).zfill(10)
    return binario, explicacao

def exibir_resultado():
    try:
        valor = int(entrada_valor.get())
        if valor < 0:
            raise ValueError("Digite um número inteiro positivo.")
        binario, passos = converter_para_binario_com_explicacao(valor)

        resultado = f"Decimal: {valor}\nBinário (10 bits): {binario}\n\nPasso a passo:\n"
        resultado += "\n".join(passos[::-1])  # Mostra de cima para baixo
        resultado_label.config(text=resultado)
    except ValueError as e:
        messagebox.showerror("Erro", str(e))

# Janela principal
janela = tk.Tk()
janela.title("Conversor Decimal → Binário com Explicação")
janela.geometry("460x500")
janela.configure(bg="#1e1e1e")

# Estilo escuro com texto claro
estilo_escuro = {
    "bg": "#1e1e1e",
    "fg": "#ffff99",
    "font": ("Courier", 10)
}

# Entrada
tk.Label(janela, text="Digite um número decimal:", **estilo_escuro).pack(pady=10)
entrada_valor = tk.Entry(janela, bg="#2e2e2e", fg="#ffff99", insertbackground="#ffff99")
entrada_valor.pack()

# Botão
tk.Button(janela, text="Converter para Binário", command=exibir_resultado, bg="#3a3a3a", fg="#ffff99").pack(pady=10)

# Resultado
resultado_label = tk.Label(janela, text="", justify="left", wraplength=440, **estilo_escuro)
resultado_label.pack(pady=10)

# Inicia
janela.mainloop()

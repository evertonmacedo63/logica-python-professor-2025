import tkinter as tk
from tkinter import messagebox

def iniciar_conversao():
    try:
        numero = int(entrada_valor.get())
        if numero < 0:
            raise ValueError("Digite um número inteiro positivo.")
        binario, passos = converter_para_binario(numero)
        animar_binario(binario, passos)
    except ValueError as e:
        messagebox.showerror("Erro", str(e))

def converter_para_binario(numero):
    restos = []
    explicacao = []

    original = numero
    while numero > 0:
        quociente = numero // 2
        resto = numero % 2
        restos.append(resto)
        explicacao.append(f"{numero} ÷ 2 = {quociente} com resto {resto}")
        numero = quociente

    binario = ['0'] * 10
    for i, bit in enumerate(reversed(restos)):
        if i < 10:
            #binario[9 - i] = str(bit)  # direita para esquerda
            binario[i + (10 - len(restos))] = str(bit)  # alinha à direita corretamente
    return binario, explicacao[::-1]

def animar_binario(binario, passos):
    canvas.delete("all")
    resultado_label.config(text="")
    largura = 30
    for i in range(10):
        canvas.create_rectangle(20 + i * largura, 20, 20 + (i + 1) * largura, 60, fill="#2e2e2e", outline="#ffff99")
        canvas.create_text(35 + i * largura, 40, text="0", fill="#ffff99", font=("Courier", 14), tag=f"bit{i}")

    def atualizar_bit(i):
        if i < len(binario):
            canvas.itemconfig(f"bit{9 - i}", text=binario[9 - i])
            janela.after(300, lambda: atualizar_bit(i + 1))
        else:
            resultado_label.config(text="\n".join(passos))

    janela.after(500, lambda: atualizar_bit(0))

# Janela principal
janela = tk.Tk()
janela.title("Animação: Decimal → Binário com Vetor")
janela.geometry("420x500")
janela.configure(bg="#1e1e1e")

# Estilo escuro
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
tk.Button(janela, text="Converter com Animação", command=iniciar_conversao, bg="#3a3a3a", fg="#ffff99").pack(pady=10)

# Canvas para vetor
canvas = tk.Canvas(janela, width=400, height=80, bg="#1e1e1e", highlightthickness=0)
canvas.pack()

# Explicação
resultado_label = tk.Label(janela, text="", justify="left", wraplength=400, **estilo_escuro)
resultado_label.pack(pady=10)

# Inicia
janela.mainloop()
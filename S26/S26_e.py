import tkinter as tk
from tkinter import messagebox, filedialog
from datetime import datetime

def iniciar_conversao():
    try:
        numero = int(entrada_valor.get())
        if numero < 0:
            raise ValueError("Digite um número inteiro positivo.")
        global binario_final, passos_final, numero_decimal
        numero_decimal = numero
        binario_final, passos_final = converter_para_binario(numero)
        animar_binario(binario_final, passos_final)
    except ValueError as e:
        messagebox.showerror("Erro", str(e))

def converter_para_binario(numero):
    restos = []
    explicacao = []

    while numero > 0:
        quociente = numero // 2
        resto = numero % 2
        restos.append(resto)
        posicao = len(restos) - 1
        linha_formatada = (
            f"{str(numero).rjust(4)} ÷ 2 = {str(quociente).rjust(4)}   "
            f"| resto: {str(resto).rjust(2)}   → casa: {str(posicao).rjust(2)}"
        )
        explicacao.append(linha_formatada)
        numero = quociente

    binario = ['0'] * 12
    for i, bit in enumerate(restos):
        if i < 12:
            binario[i] = str(bit)
    return binario, explicacao

def animar_binario(binario, passos):
    canvas.delete("all")
    resultado_label.config(text="")
    vetor_label.config(text="")
    largura = 30

    for i in range(12):
        canvas.create_rectangle(20 + i * largura, 20, 20 + (i + 1) * largura, 60,
                            fill="#2e2e2e", outline="#ffff99")
        canvas.create_text(35 + i * largura, 40, text="0",
                       fill="#ffff99", font=("Courier", 14), tag=f"bit{i}")
        canvas.create_text(35 + i * largura, 70, text=str(11 - i),
                   fill="#666666", font=("Courier", 9))
    

    def mostrar_passo(i):
        if i < len(passos):
            resultado_label.config(text=passos[i])
            janela.after(800, lambda: preencher_bit(i))
        else:
            resultado_label.config(text="\n".join(passos))
            vetor_visual = ' '.join(reversed(binario))
            vetor_label.config(text=f"Vetor visual: {vetor_visual}")

    def preencher_bit(i):
        posicao_visual = 11 - i
        canvas.itemconfig(f"bit{posicao_visual}", text=binario[i],
                          fill="#ffffff", font=("Courier", 14, "bold"))
        janela.after(800, lambda: mostrar_passo(i + 1))

    janela.after(500, lambda: mostrar_passo(0))

def limpar():
    entrada_valor.delete(0, tk.END)
    resultado_label.config(text="")
    vetor_label.config(text="")
    canvas.delete("all")
    largura = 30
    for i in range(12):
        canvas.create_rectangle(20 + i * largura, 20, 20 + (i + 1) * largura, 60,
                                fill="#2e2e2e", outline="#ffff99")
        canvas.create_text(35 + i * largura, 40, text="0",
                           fill="#ffff99", font=("Courier", 14), tag=f"bit{i}")

def exportar():
    if not binario_final or not passos_final:
        messagebox.showwarning("Aviso", "Nenhuma conversão foi feita ainda.")
        return

    binario_str = ''.join(reversed(binario_final))
    binario_visual = ' '.join(reversed(binario_final))
    data_hora = datetime.now().strftime("%d-%m-%Y-%H-%M-%S")
    nome_arquivo = f"Conversao_{data_hora}.txt"

    caminho = filedialog.asksaveasfilename(defaultextension=".txt", initialfile=nome_arquivo,
                                           filetypes=[("Arquivo de texto", "*.txt")])
    if caminho:
        with open(caminho, "w", encoding="utf-8") as f:
            f.write("Implementação assistida por IA e revisada por Prof. Everton Macedo - S26-plus\n")
            f.write("=" * 70 + "\n")
            f.write(f"Número decimal: {numero_decimal}\n")
            f.write(f"Binário (12 bits): {binario_str}\n")
            f.write(f"Vetor visual: {binario_visual}\n\n")
            f.write("Passo a passo da conversão:\n")
            for linha in passos_final:
                f.write(linha + "\n")
        messagebox.showinfo("Exportado", f"Arquivo salvo como:\n{caminho}")

# Variáveis globais
binario_final = []
passos_final = []
numero_decimal = 0

# Janela principal
janela = tk.Tk()
janela.title("Animação Educativa: Decimal → Binário")
janela.geometry("460x640")
janela.configure(bg="#1e1e1e")

estilo_escuro = {
    "bg": "#1e1e1e",
    "fg": "#ffff99",
    "font": ("Courier", 10)
}

tk.Label(janela, text="Digite um número decimal:", **estilo_escuro).pack(pady=10)
entrada_valor = tk.Entry(janela, bg="#2e2e2e", fg="#ffff99", insertbackground="#ffff99")
entrada_valor.pack()

frame_botoes = tk.Frame(janela, bg="#1e1e1e")
frame_botoes.pack(pady=10)

tk.Button(frame_botoes, text="Converter com Animação", command=iniciar_conversao,
          bg="#3a3a3a", fg="#ffff99").grid(row=0, column=0, padx=5)

tk.Button(frame_botoes, text="Limpar", command=limpar,
          bg="#3a3a3a", fg="#ffff99").grid(row=0, column=1, padx=5)

tk.Button(frame_botoes, text="Exportar", command=exportar,
          bg="#3a3a3a", fg="#ffff99").grid(row=0, column=2, padx=5)

canvas = tk.Canvas(janela, width=420, height=80, bg="#1e1e1e", highlightthickness=0)
canvas.pack()

resultado_label = tk.Label(janela, text="", justify="left", wraplength=440, **estilo_escuro)
resultado_label.pack(pady=10)

vetor_label = tk.Label(janela, text="", justify="left", wraplength=440, **estilo_escuro)
vetor_label.pack(pady=5)

assinatura_label1 = tk.Label(
    janela,
    text="Implementação assistida por IA",
    bg="#1e1e1e",
    fg="#666666",
    font=("Courier", 9)
)
assinatura_label1.pack()

assinatura_label2 = tk.Label(
    janela,
    text="Revisada por Prof. Everton Macedo - S26-plus",
    bg="#1e1e1e",
    fg="#666666",
    font=("Courier", 9)
)
assinatura_label2.pack(pady=5)

janela.mainloop()
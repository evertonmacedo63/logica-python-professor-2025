import tkinter as tk
from tkinter import messagebox, filedialog

def gerar_vetor_dobro(valor_inicial, tamanho=10):
    vetor = [valor_inicial]
    for _ in range(1, tamanho):
        vetor.append(vetor[-1] * 2)
    return vetor

def converter_para_binario(vetor):
    return [bin(valor)[2:] for valor in vetor]  # Remove o prefixo '0b'

def exibir_resultado():
    try:
        V = int(entrada_valor.get())
        if V < 0 or V > 50:
            raise ValueError("Valor fora do intervalo permitido (0 a 50).")
        vetor = gerar_vetor_dobro(V)
        binarios = converter_para_binario(vetor)
        resultado_texto = "\n".join([f"N[{i}] = {valor}   Binário: {binarios[i]}" for i, valor in enumerate(vetor)])
        resultado_label.config(text=resultado_texto)
        botao_exportar.config(state="normal")
        janela.vetor_gerado = resultado_texto
    except ValueError as e:
        messagebox.showerror("Erro", str(e))

def exportar_para_txt():
    caminho = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Arquivo de texto", "*.txt")])
    if caminho:
        with open(caminho, "w") as arquivo:
            arquivo.write(janela.vetor_gerado)
        messagebox.showinfo("Exportado", f"Arquivo salvo em:\n{caminho}")

# Janela principal
janela = tk.Tk()
janela.title("Gerador de Vetor Dobrado com Binário")
janela.geometry("400x500")
janela.configure(bg="#1e1e1e")  # Tema escuro

# Estilo escuro com texto amarelo claro
estilo_escuro = {
    "bg": "#1e1e1e",
    "fg": "#ffff99",
    "font": ("Courier", 10)
}

# Entrada de valor
tk.Label(janela, text="Digite um valor inteiro (até 50):", **estilo_escuro).pack(pady=10)
entrada_valor = tk.Entry(janela, bg="#2e2e2e", fg="#ffff99", insertbackground="#ffff99")
entrada_valor.pack()

# Botão de gerar
tk.Button(janela, text="Gerar Vetor", command=exibir_resultado, bg="#3a3a3a", fg="#ffff99").pack(pady=10)

# Área de resultado
resultado_label = tk.Label(janela, text="", justify="left", wraplength=350, **estilo_escuro)
resultado_label.pack(pady=10)

# Botão de exportar
botao_exportar = tk.Button(janela, text="Exportar para .txt", command=exportar_para_txt, bg="#3a3a3a", fg="#ffff99")
botao_exportar.pack(pady=10)
botao_exportar.config(state="disabled")

# Inicia a interface
janela.mainloop()

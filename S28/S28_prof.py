import tkinter as tk
from tkinter import messagebox

def converter():
    base_str = base_entry.get()
    numero_str = numero_entry.get()

    try:
        base = int(base_str)
        if not (2 <= base <= 36):
            raise ValueError("Base fora do intervalo permitido.")

        # Converte o número da base informada para decimal
        decimal = int(numero_str, base)

        # Converte o número decimal para binário
        binario = bin(decimal)[2:]  # remove o prefixo '0b'

        resultado_label.config(text=f"Decimal: {decimal}\nBinário: {binario}")
    except ValueError as e:
        messagebox.showerror("Erro", f"Entrada inválida: {e}")

# Interface gráfica
root = tk.Tk()
root.title("Conversor de Base para Binário")

tk.Label(root, text="Informe a base (2 a 36):").pack()
base_entry = tk.Entry(root)
base_entry.pack()

tk.Label(root, text="Informe o número na base escolhida:").pack()
numero_entry = tk.Entry(root)
numero_entry.pack()

tk.Button(root, text="Converter", command=converter).pack(pady=10)

resultado_label = tk.Label(root, text="", font=("Courier", 12))
resultado_label.pack()

root.mainloop()
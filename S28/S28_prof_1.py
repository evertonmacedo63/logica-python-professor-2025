import tkinter as tk
from tkinter import ttk, messagebox

def converter():
    try:
        decimal = int(decimal_entry.get())
        base = int(base_combobox.get())

        # Converte para a base escolhida
        if base == 2:
            convertido = bin(decimal)[2:]
        elif base == 8:
            convertido = oct(decimal)[2:]
        elif base == 16:
            convertido = hex(decimal)[2:].upper()
        else:
            raise ValueError("Base inválida")

        # Reconversão explicada
        explicacao = ""
        potencia = len(convertido) - 1
        total = 0

        for i, digito in enumerate(convertido):
            if base == 16 and digito.isalpha():
                valor = ord(digito.upper()) - ord('A') + 10
            else:
                valor = int(digito)

            peso = base ** potencia
            parcial = valor * peso
            total += parcial
            explicacao += f"{digito} × {base}^{potencia} = {parcial}\n"
            potencia -= 1

        resultado_label.config(
            text=f"Convertido para base {base}: {convertido}\n\nReconversão para decimal:\n{explicacao}Total: {total}"
        )

        desenhar_digitos(convertido)

    except ValueError as e:
        messagebox.showerror("Erro", f"Entrada inválida: {e}")

def desenhar_digitos(digitos):
    canvas.delete("all")
    x = 10
    y = 20
    for d in digitos:
        cor = "lightblue" if d.isdigit() else "orange"
        canvas.create_rectangle(x, y, x+40, y+40, fill=cor, outline="black")
        canvas.create_text(x+20, y+20, text=d, font=("Arial", 14, "bold"))
        x += 50

# Interface gráfica
root = tk.Tk()
root.title("Conversor Pedagógico com Visualização")

tk.Label(root, text="Informe um número em base 10:").pack()
decimal_entry = tk.Entry(root)
decimal_entry.pack()

tk.Label(root, text="Escolha a base de destino:").pack()
base_combobox = ttk.Combobox(root, values=["2", "8", "16"])
base_combobox.pack()
base_combobox.set("2")

tk.Button(root, text="Converter", command=converter).pack(pady=10)

resultado_label = tk.Label(root, text="", font=("Courier", 12), justify="left")
resultado_label.pack(padx=10, pady=10)

canvas = tk.Canvas(root, width=600, height=80, bg="white")
canvas.pack(pady=10)

root.mainloop()
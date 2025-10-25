import tkinter as tk
import random
import copy

class Jogo2048:
    def __init__(self, master):
        self.master = master
        self.master.title("2048 - Desafio Numérico")
        self.tamanho = 4
        self.tabuleiro = [[0]*self.tamanho for _ in range(self.tamanho)]
        self.tabuleiro_anterior = None
        self.pode_desfazer = True
        self.contador_jogadas = 0

        # Interface gráfica
        self.frame = tk.Frame(master)
        self.frame.pack()
        self.labels = [[tk.Label(self.frame, width=4, height=2, font=("Arial", 24), bg="lightgray", relief="ridge") for _ in range(self.tamanho)] for _ in range(self.tamanho)]
        for i in range(self.tamanho):
            for j in range(self.tamanho):
                self.labels[i][j].grid(row=i, column=j, padx=5, pady=5)

        self.label_contador = tk.Label(master, text="Jogadas: 0")
        self.label_contador.pack()

        self.instrucoes = tk.Label(master, text="Use W/A/S/D ou setas para mover. Clique em 'Desfazer' uma vez por rodada. Pressione F1 para ver as regras.")
        self.instrucoes.pack()

        self.botao_desfazer = tk.Button(master, text="Desfazer", command=self.desfazer)
        self.botao_desfazer.pack()

        self.botao_demo = tk.Button(master, text="Modo Demo", command=self.modo_demo)
        self.botao_demo.pack()

        self.botao_sair = tk.Button(master, text="Sair", command=master.quit)
        self.botao_sair.pack()

        self.master.bind("<Key>", self.tratar_tecla)
        self.master.bind("<F1>", self.mostrar_regras)

        self.gerar_bloco()
        self.gerar_bloco()
        self.atualizar_interface()

    def gerar_bloco(self):
        vazio = [(i, j) for i in range(self.tamanho) for j in range(self.tamanho) if self.tabuleiro[i][j] == 0]
        if vazio:
            i, j = random.choice(vazio)
            self.tabuleiro[i][j] = random.choice([2, 4, 8])

    def tratar_tecla(self, evento):
        direcoes = {
            "Up": self.mover_cima,
            "Down": self.mover_baixo,
            "Left": self.mover_esquerda,
            "Right": self.mover_direita,
            "w": self.mover_cima,
            "s": self.mover_baixo,
            "a": self.mover_esquerda,
            "d": self.mover_direita
        }
        tecla = evento.keysym.lower()
        if tecla in direcoes:
            self.tabuleiro_anterior = copy.deepcopy(self.tabuleiro)
            if direcoes[tecla]():
                self.gerar_bloco()
                self.pode_desfazer = True
                self.contador_jogadas += 1
                self.label_contador["text"] = f"Jogadas: {self.contador_jogadas}"
            self.atualizar_interface()

    def mover_esquerda(self):
        return self.mover(lambda linha: linha)

    def mover_direita(self):
        return self.mover(lambda linha: linha[::-1], reverse=True)

    def mover_cima(self):
        self.tabuleiro = [list(x) for x in zip(*self.tabuleiro)]
        mudou = self.mover(lambda linha: linha)
        self.tabuleiro = [list(x) for x in zip(*self.tabuleiro)]
        return mudou

    def mover_baixo(self):
        self.tabuleiro = [list(x) for x in zip(*self.tabuleiro)]
        mudou = self.mover(lambda linha: linha[::-1], reverse=True)
        self.tabuleiro = [list(x) for x in zip(*self.tabuleiro)]
        return mudou

    def mover(self, transformador, reverse=False):
        mudou = False
        novo_tabuleiro = []
        for linha in self.tabuleiro:
            original = linha[:]
            linha = transformador(linha)
            linha = self.comprimir(linha)
            linha = self.juntar(linha)
            linha = self.comprimir(linha)
            if reverse:
                linha = linha[::-1]
            novo_tabuleiro.append(linha)
            if linha != original:
                mudou = True
        self.tabuleiro = novo_tabuleiro
        return mudou

    def comprimir(self, linha):
        nova = [n for n in linha if n != 0]
        nova += [0] * (self.tamanho - len(nova))
        return nova

    def juntar(self, linha):
        for i in range(self.tamanho - 1):
            if linha[i] != 0 and linha[i] == linha[i + 1]:
                linha[i] *= 2
                linha[i + 1] = 0
        return linha

    def desfazer(self):
        if self.pode_desfazer and self.tabuleiro_anterior:
            self.tabuleiro = self.tabuleiro_anterior
            self.pode_desfazer = False
            self.atualizar_interface()

    def atualizar_interface(self):
        for i in range(self.tamanho):
            for j in range(self.tamanho):
                valor = self.tabuleiro[i][j]
                self.labels[i][j]["text"] = str(valor) if valor != 0 else ""
                self.labels[i][j]["bg"] = self.cor_bloco(valor)

    def cor_bloco(self, valor):
        cores = {
            0: "lightgray", 2: "#eee4da", 4: "#ede0c8", 8: "#f2b179",
            16: "#f59563", 32: "#f67c5f", 64: "#f65e3b", 128: "#edcf72",
            256: "#edcc61", 512: "#edc850", 1024: "#edc53f", 2048: "#edc22e"
        }
        return cores.get(valor, "#3c3a32")

    def movimentos_possiveis(self):
        for direcao in [self.mover_esquerda, self.mover_direita, self.mover_cima, self.mover_baixo]:
            copia = copy.deepcopy(self.tabuleiro)
            if direcao():
                self.tabuleiro = copia
                return True
            self.tabuleiro = copia
        return False

    def modo_demo(self):
        def jogar():
            if not self.movimentos_possiveis():
                self.instrucoes["text"] = "Fim de jogo! Nenhum movimento possível."
                return
            for direcao in [self.mover_esquerda, self.mover_cima, self.mover_direita, self.mover_baixo]:
                copia = copy.deepcopy(self.tabuleiro)
                if direcao():
                    self.gerar_bloco()
                    self.atualizar_interface()
                    self.master.after(300, jogar)
                    return
            self.instrucoes["text"] = "Modo Demo encerrado."
        jogar()

    def mostrar_regras(self, evento=None):
        regras = tk.Toplevel(self.master)
        regras.title("Regras do Jogo 2048")
        texto = (
            "Objetivo:\n"
            "Combine blocos iguais para formar o número 2048.\n\n"
            "Como jogar:\n"
            "- Use as teclas W/A/S/D ou as setas para mover os blocos.\n"
            "- Blocos iguais se fundem ao colidir.\n"
            "- Após cada jogada, um novo bloco aparece.\n"
            "- O jogo termina quando não há mais movimentos possíveis.\n\n"
            " Recursos:\n"
            "- Botão 'Desfazer' permite voltar uma jogada.\n"
            "- Botão 'Modo Demo' mostra uma simulação automática.\n"
        )
        label = tk.Label(regras, text=texto, justify="left", padx=10, pady=10, font=("Arial", 12))
        label.pack()

if __name__ == "__main__":
    root = tk.Tk()
    jogo = Jogo2048(root)
    root.mainloop()
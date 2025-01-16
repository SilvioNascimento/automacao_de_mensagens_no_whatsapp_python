import tkinter as tk
from threading import Thread

def iniciar_contagem(tempo_restante: int):
    def criar_janela():
        # Função auxiliar para a contagem regressiva
        def atualizar_tempo(tempo):
            if tempo >= 0:
                label.config(
                    text=f"""Tempo restante: {tempo} segundos. 
Não faça nenhuma ação no PC!"""
                )
                janela.after(1000, atualizar_tempo, tempo - 1)
            else:
                label.config(text="Tempo esgotado!")
                janela.after(1000, janela.destroy)  # Fecha a janela após o fim da contagem

        # Criação da janela
        janela = tk.Tk()
        janela.title("⏱ Contagem Regressiva ⏱")
        janela.geometry("350x150")

        # Label para exibir a contagem
        label = tk.Label(janela, text="", font=("Helvetica", 14))
        label.pack(pady=40)
        
        # Força a janela a ficar no topo e ter foco
        janela.attributes("-topmost", True)
        janela.focus_force()

        # Iniciar contagem
        atualizar_tempo(tempo_restante)

        # Iniciar o loop da janela
        janela.mainloop()

    # Inicia a janela do temporizador em uma nova thread
    Thread(target=criar_janela).start()

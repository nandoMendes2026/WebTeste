import tkinter as tk

def botao_clicado():
    print("Botão clicado!")
    rotulo.configure(text="Botão foi clicado!", background="#108810")

janela = tk.Tk()
janela.title("Minha GUI com botão")

rotulo = tk.Label(janela, text="Clique no botão:")
rotulo.pack()

botao = tk.Button(janela, text="Clique aqui", command=botao_clicado)
botao.pack()

janela.mainloop()
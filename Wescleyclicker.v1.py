from tkinter import *
import time
import threading as thr

def formatar(x):
    if x >= 1000000000:
        return f"{x / 1000000000:.1f}B"
    elif x >= 1000000:
        return f"{x / 1000000:.1f}M"
    elif x >= 1000:
        return f"{x / 1000:.1f}K"
    else:
        return f"{x:.1f}"   
def adicionar_ferros():
    global ferros
    ferros += 1
    vezes.config(text=f"Há {formatar(ferros)} ferros nas pernas do Wescley")
def abrir_loja():
    loja.pack(pady=20)
    botao_abrir_loja.pack_forget()
def fechar_loja():
    loja.pack_forget()
    botao_abrir_loja.pack(pady=20)
def botao500():
    global ferros
    global estagiarios
    if ferros >= 500:
        ferros -= 500
        vezes.config(text=f"Há {formatar(ferros)} ferros nas pernas do Wescley")
        estagiarios += 1
        estagiario_item.config(text=f"Estagiário ({estagiarios}x)")
def estagiario_habilidade():
    global estagiarios, ferros
    while True:
        if estagiarios > 0:
            multiplicador = estagiarios * estagiario_eficiencia
            ferros += multiplicador
            vezes.config(text=f"Há {formatar(ferros)} ferros nas pernas do Wescley")
        time.sleep(1)
def botao1000():
    global ferros, estagiario_eficiencia
    if ferros >= 1000:
        ferros -= 1000
        vezes.config(text=f"Há {formatar(ferros)} ferros nas pernas do Wescley")
        estagiario_eficiencia += 0.1
        eficiencia_item.config(text=f"Eficiência ({formatar(estagiario_eficiencia)}x)")


janela = Tk()
janela.title("Wescley Clicker")
janela.geometry("800x900")

introducao = Label(janela, text="Wescley precisa ajeitar suas pernas!", font=("Arial", 28))
introducao.pack(pady=(210, 20))

ferros = 0
estagiarios = 0
estagiario_eficiencia = 1

vezes = Label(janela, text=f"Há {formatar(ferros)} ferros nas pernas dos Wescley", font=("Arial", 20))
vezes.pack(pady=(0, 20))

botao = Button(janela, text="Colocar ferros", command=adicionar_ferros, font=("Arial", 16), bg="lightgray", activebackground="gray")
botao.pack()


loja = Frame(janela)
loja.pack_forget()
introducao_loja = Label(loja, text="Bem-vindo à Loja!", font=("Arial", 20))
introducao_loja.pack(pady=(80, 10))

estagiario_item = Label(loja, text=f"Estagiário ({formatar(estagiarios)}x)", font=("Arial", 16))
estagiario_item.pack(pady=10)
botao_estagiario = Button(loja, text="500 ferros", command=botao500, font=("Arial", 16), bg="lightgray", activebackground="gray")
botao_estagiario.pack(pady=10)

eficiencia_item = Label(loja, text=f"Eficiência ({formatar(estagiario_eficiencia)}x)", font=("Arial", 16))
eficiencia_item.pack(pady=10)
botao_eficiencia = Button(loja, text="1000 ferros", command=botao1000, font=("Arial", 16), bg="lightgray", activebackground="gray")
botao_eficiencia.pack(pady=10)

botao_fechar_loja = Button(loja, text="Fechar", command = fechar_loja, font=("Arial", 16), bg="lightgray", activebackground="gray")
botao_fechar_loja.pack(pady=10)

botao_abrir_loja = Button(janela, text="Abrir loja", command= abrir_loja, font=("Arial", 16), bg="lightgray", activebackground="gray")
botao_abrir_loja.pack(pady=10)


thread_estagiarios = thr.Thread(target=estagiario_habilidade, daemon=True)
thread_estagiarios.start()

janela.mainloop()

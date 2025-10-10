import tkinter as tk
from tkinter import messagebox


janela = tk.Tk()
janela.title("Interface Gráfica com Tkinter")
janela.geometry("600x400")

def mostrar_mensagem():
    messagebox.showinfo("Mensagem", "Olá! Teste Tkinter.")
    janela.configure(bg="lightblue")
botao = tk.Button(janela, text="Clique Aqui", command=mostrar_mensagem)
botao.pack(pady=20)
janela.mainloop()
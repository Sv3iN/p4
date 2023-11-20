#pip install customtkinter
#pip install packaging

import customtkinter as ctk
from tkinter import *
import lib


def abrir_janela():
    tela_lista = ctk.CTkToplevel()
    tela_lista.geometry("700x500")
    tela_lista.title("Listagem de candidato")
    tela_lista.resizable(False, False)
    L_label = ctk.CTkLabel(tela_lista, text='Digite as notas para a busca', font = ('Roboto', 14, 'bold'), text_color= ('white') )
    L_label.place(x=250, y=5)
    P_entrevista = ctk.CTkEntry(tela_lista, placeholder_text="Entrevista", width=100)
    P_entrevista.place(x=170, y=35)
    P_teorico = ctk.CTkEntry(tela_lista, placeholder_text="Teste teórico", width=100)
    P_teorico.place(x=275, y=35)
    P_pratico = ctk.CTkEntry(tela_lista, placeholder_text="Teste prático", width=100)
    P_pratico.place(x=380, y=35)
    P_soft = ctk.CTkEntry(tela_lista, placeholder_text="Soft skill", width=100)
    P_soft.place(x=485, y=35)
    button_fechar = ctk.CTkButton(tela_lista, text="Fechar",width=100, command=tela_lista.destroy)
    button_fechar.place(x=15, y=5)
    lista = ctk.CTkTextbox(tela_lista, width=550, height=300)
    lista.place(x=95, y=85)
    
    

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

tela_cad = ctk.CTk()
tela_cad.geometry("700x500")
tela_cad.title("Cadastro de candidato")
tela_cad.resizable(False, False)

frame = ctk.CTkFrame(master=tela_cad, width=320, height=600)
frame.pack(side=TOP)
label = ctk.CTkLabel(master=frame, text='Cadastro de candidato', font = ('Roboto', 20, 'bold'), text_color= ('white') )
label.place(x=50, y=5)

def cad():
    nome = str(entry1.get())
    telefone = int(entry2.get())
    minibio = str(entry3.get())
    entrevista = int(entry4.get())
    teste_teorico = int(entry5.get())
    teste_pratico = int(entry6.get())
    avaliação_softskill = int(entry7.get())
    lib.Candidato.cadastrar(nome, telefone, minibio, entrevista, teste_teorico, teste_pratico, avaliação_softskill)


entry1 = ctk.CTkEntry(master=frame, placeholder_text="Nome", width=265)
entry1.place(x=25, y=85)

entry2 = ctk.CTkEntry(master=frame, placeholder_text="Telefone", width=265)
entry2.place(x=25, y=130)

entry3 = ctk.CTkEntry(master=frame, placeholder_text="Minibio", width=265)
entry3.place(x=25, y=175)

entry4 = ctk.CTkEntry(master=frame, placeholder_text="Entrevista", width=265)
entry4.place(x=25, y=220)

entry5 = ctk.CTkEntry(master=frame, placeholder_text="Teste teórico", width=265)
entry5.place(x=25, y=270)

entry6 = ctk.CTkEntry(master=frame, placeholder_text="Teste prático", width=265)
entry6.place(x=25, y=320)

entry7 = ctk.CTkEntry(master=frame, placeholder_text="Soft skill", width=265)
entry7.place(x=25, y=365)

button = ctk.CTkButton(master=frame, text="Cadastrar", command=cad, width=265)
button.place(x=25, y=420)
button_abrir = ctk.CTkButton(tela_cad, text="Listagem de candidato",width=100, command=abrir_janela)
button_abrir.place(x=15, y=25)

tela_cad.mainloop()
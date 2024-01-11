import customtkinter
from tkinter import *

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

# passo 1 
janela = customtkinter.CTk()
janela.geometry("700x400")
janela.title("Sistema Supera")
janela.iconbitmap("icone.ico")
janela.resizable(False, False)

#-passo 2
img = PhotoImage(file="fundo.png")
label_img = customtkinter.CTkLabel(master=janela, image=img)
label_img.place(x=20, y=85)

#-passo 3
frame = customtkinter.CTkFrame( master=janela, width=355, height=396)
frame.pack(side=RIGHT)

#-passo 4 Titulo
label = customtkinter.CTkLabel( master=frame, text="Bem vindo", width=120, height=60 )
label.place(x=25, y=5)

# passo 5 Input_email
input_email = customtkinter.CTkEntry( master=frame, placeholder_text="Nome de usuário", width=300 )
input_email.place(x=25, y=105)

label_email = customtkinter.CTkLabel( master=frame, text="O campo nome de usuário é obrigatório",  text_color="green" )
label_email.place(x=25, y=135)

# passo 6 Input_senha
input_email = customtkinter.CTkEntry( master=frame, placeholder_text="Senha de usuário", width=300 )
input_email.place(x=25, y=180)

label_email = customtkinter.CTkLabel( master=frame, text="O campo senha de usuário é obrigatório",  text_color="green" )
label_email.place(x=25, y=210)

chekbox = customtkinter.CTkCheckBox(master=frame, text="lembr-se de min sempre").place(x=25, y=250)

button = customtkinter.CTkButton(master=frame, text="LOGIN", width=300).place(x=25, y=250)

janela.mainloop()

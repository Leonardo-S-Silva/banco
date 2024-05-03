import customtkinter
from tkinter import *

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

janela = customtkinter.CTk()
janela.geometry("700x500")
janela.title("Beta-Login")
janela.iconbitmap("icon.ico")
janela.resizable(False, False)

#trabalhando com a imagem da tela
img = PhotoImage(file="log.png")
label_img = customtkinter.CTkLabel(master=janela, image=img)
label_img.place(x=0, y=55)

label_tt = customtkinter.CTkLabel(master=janela, text="Entre com sua conta em nossa plataforma\n e viva uma experiencia incrivel.", text_color="#00B0F0")
label_tt.place(x=10, y=10)
label_tt.configure(font=("Roboto", 18))


#frame
frame = customtkinter.CTkFrame(master=janela, width=350, height=396)
frame.pack(side=RIGHT)

#frame widgets
label = customtkinter.CTkLabel(master=frame, text="Sistema de login")
label.configure(font=("Roboto", 20))
label.place(x=25, y=5)

entry1 = customtkinter.CTkEntry(master=frame, placeholder_text="Nome do usuário", width=300).place(x=25, y=105)
label1 = customtkinter.CTkLabel(master=frame, text=" Campo NOME DO USUÁRIO é de carater obrigatório.", text_color="green").place(x=25, y=135)
label.configure(font=("Roboto", 20))


entry2 = customtkinter.CTkEntry(master=frame, placeholder_text="Senha do usuário", width=300).place(x=25, y=185)
label2 = customtkinter.CTkLabel(master=frame, text=" Campo SENHA DO USUÁRIO é de carater obrigatório.", text_color="green").place(x=25, y=215)
label.configure(font=("Roboto", 20))


chekbox = customtkinter.CTkCheckBox(master=frame, text="Marque aqui para lembrar a senha").place(x=25, y=255)

button = customtkinter.CTkButton(master=frame, text="LOGIN", width=300).place(x=25, y=295)

janela.mainloop()
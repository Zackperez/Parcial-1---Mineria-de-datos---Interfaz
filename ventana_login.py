from app import *
import tkinter as tk
from tkinter import *
from Controlador.ventana_principal_controlador import *

class Ventana_Login:
    def __init__(self):
        self.ventana_login = tk.Tk()
        self.configurar_ventana()
        self.decorar_ventana()
        self.ventana_login.mainloop()

    def configurar_ventana(self):
        self.ventana_login.config(bg = "#0D1216")
        self.ventana_login.title("Login")
        self.ventana_login.resizable(0,0)
        self.dimensiones_ventana()

    def dimensiones_ventana(self):
        wventana = 610
        hventana = 600
        wtotal = self.ventana_login.winfo_screenwidth()
        htotal = self.ventana_login.winfo_screenheight()
        pwidth = round(wtotal/2-wventana/2)
        pheight = round(htotal/2-hventana/2)
        self.ventana_login.geometry(str(wventana)+"x"+str(hventana)+"+"+str(pwidth)+"+"+str(pheight))

    def decorar_ventana(self):
        #Simple label que indica la descripcion del programa
        self.lbl_titulo_descripcion = tk.Label(self.ventana_login, text="Iniciar sesión")
        self.lbl_titulo_descripcion.config(bg="#0D1216", fg = "#FFBD59", font=('Roboto', '25', 'bold'))
        self.lbl_titulo_descripcion.grid(row=0, column=0)

        self.lbl_nombre_usuario=tk.Label(self.ventana_login,text = "Nombre de usuario" )
        self.lbl_nombre_usuario.config(bg="#0D1216", fg = "white", font = ('Roboto', '12',))
        self.lbl_nombre_usuario.grid(row = 2, column = 0, pady=5)
        
        self.txt_nombre_usuario = tk.Entry(self.ventana_login, relief="solid")
        self.txt_nombre_usuario.grid(row = 3, column = 0, ipadx = 20, padx = 10)

        self.lblPregunta=tk.Label(self.ventana_login,text = "Contraseña" )
        self.lblPregunta.config(bg="#0D1216", fg = "white", font = ('Roboto', '12',))
        self.lblPregunta.grid(row = 4, column = 0, pady=5)
        
        self.txt_password_usuario = tk.Entry(self.ventana_login, relief="solid")
        self.txt_password_usuario.grid(row = 5, column = 0, ipadx = 20, padx = 10)

        self.btnEnviar = tk.Button(self.ventana_login, text = "Iniciar sesión", width = 10, height = 1)
        self.btnEnviar.grid(row = 6, column = 0, pady = 5)
        self.btnEnviar.config(command = self.mostrar_usuario)


    def mostrar_usuario(self):
        usuario = self.txt_nombre_usuario.get()
        password = self.txt_password_usuario.get()
        print(usuario)

        if usuario == "Jean" and password == "3008":
        #Inicializador de ventanas
            self.iniciar_ventana_principal()
        else:
            print("Datos erróneos")

    def iniciar_ventana_principal(self):
        root = tk.Tk()
        Ventana_Principal_Controlador(root)
        root.mainloop()

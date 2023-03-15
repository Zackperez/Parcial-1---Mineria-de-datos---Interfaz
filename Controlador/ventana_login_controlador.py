import tkinter as tk
from Modelo.ventana_login_modelo import *
from ventana_login import *


class Ventana_Login_Controlador:

    def __init__(self, root):
        self.model = Ventana_Login_Modelo()
        self.view = Ventana_Login(root)

        self.view.btnGuardar_texto_escrito.config()
        self.view.btnEnviar.config(command= self.iniciar_sesion)

        

    def iniciar_sesion(self):
        nombre_usuario = self.view.txt_nombre_usuario.get()
        password = self.view.txt_password_usuario.get()

        print(nombre_usuario)
        print(password)


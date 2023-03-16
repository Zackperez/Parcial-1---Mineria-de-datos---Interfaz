import tkinter as tk
from Modelo.ventana_login_modelo import *
from ventana_login import *

class Ventana_Login_Controlador:

    def __init__(self):
        self.model = Ventana_Login_Modelo()
        self.view = Ventana_Login()

        self.view.btnEnviar.config(command = mostrar_usuario)
        usuario = self.view.txt_nombre_usuario.get()

        def mostrar_usuario():
            print(usuario)



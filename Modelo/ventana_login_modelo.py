from ventana_login import *

class Ventana_Login_Modelo:

    def __init__(self):
        self.nombre_usuario = tk.StringVar()
        self.password = tk.StringVar() 

    def get_nombre_usuario(self):
        return self.nombre_usuario

    def set_nombre_usuario(self, nombre_usuario):
        self.nombre_usuario = nombre_usuario

    def get_password_usuario(self):
        return self.password_usuario

    def set_password_usuario(self, password_usuario):
        self.password_usuario = password_usuario
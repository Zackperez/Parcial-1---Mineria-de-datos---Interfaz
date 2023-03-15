import tkinter as tk
from tkinter import *

class Ventana_Principal:

    def __init__(self):
        self.ventana_principal = tk.Tk()
        self.decorar_ventana()
        self.configurar_ventana()


        self.dimensiones_ventana()
        self.menu()
        #Tiene que quedar de último
        self.ventana_principal.mainloop()


    #Botones, menu, labels, entre otros
    def decorar_ventana(self):
        self.boton_salir = tk.Button(text = "Crea el ID", command = "", state = NORMAL)
        self.boton_salir.grid(row = 0, column = 0)

    #Configuraciones generales de la ventana
    def configurar_ventana(self):
        self.ventana_principal.config(bg = "#0D1216")
        self.ventana_principal.title("Menu principal")
        self.dimensiones_ventana()

    def dimensiones_ventana(self):
        wventana = 610
        hventana = 600
        wtotal = self.ventana_principal.winfo_screenwidth()
        htotal = self.ventana_principal.winfo_screenheight()
        pwidth = round(wtotal/2-wventana/2)
        pheight = round(htotal/2-hventana/2)
        self.ventana_principal.geometry(str(wventana)+"x"+str(hventana)+"+"+str(pwidth)+"+"+str(pheight))

    #Menu principal
    def menu(self):
        self.menu = tk.Menu(self.ventana_principal)
        self.opciones = tk.Menu(self.menu)
        self.opciones.add_command(label = "Insertar")
        self.opciones.add_command(label = "Visualizar")
        self.opciones.add_command(label = "Acerca de")
        self.menu.add_cascade(label = "Opciones", menu = self.opciones)
        self.ventana_principal.config(menu = self.menu)



    
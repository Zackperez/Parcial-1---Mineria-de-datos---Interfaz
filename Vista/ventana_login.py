from ..app import *
from tkinter import ttk
import tkinter as tk
from tkinter import *

class Ventana_Login(tk.Frame):

    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.configu
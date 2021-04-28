#-*- coding: utf-8 -*-
import tkinter as tk
from tkinter import ttk
from tkinter import *

class Bitacora:

    def __init__(self, idUsuario,engine):
        self.engine=engine
        self.idUsuario=idUsuario
        self.pantallaBitacora = Tk()
        self.pantallaBitacora.title("Bitacora")
        label1 = tk.Label(self.pantallaBitacora,text="Bitacora", font=("Arial",30)).grid(row=0, columnspan=3)
        # columnas del arbol
        columnas = ('Posicion', 'ID', 'Nombre','Accion','Fecha')
        # Se crea el arbol de las puntuaciones
        self.listBox = ttk.Treeview(self.pantallaBitacora, columns=columnas, show='headings')
        # Se establece encabezado de columna
        for col in columnas:
            self.listBox.heading(col, text=col)    
        self.listBox.grid(row=1, column=0, columnspan=2)

        mostrarScores = tk.Button(self.pantallaBitacora,text="Mostrar Bitacora", width=15, command=self.show).grid(row=4, column=0)
        CerrarBtn = tk.Button(self.pantallaBitacora,text="Atras", width=15, command=self.atras).grid(row=4, column=1)
        self.pantallaBitacora.mainloop()

    def show(self):
       
        tempLista = self.engine.obtenerBitacora()

        for i, (ID,Nombre,Accion,Fecha) in enumerate(tempLista, start=1):
            self.listBox.insert("", "end", values=(i,ID,Nombre,Accion,Fecha))

    def atras(self):
        self.pantallaBitacora.destroy()
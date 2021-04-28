#-*- coding: utf-8 -*-
import tkinter as tk
from tkinter import ttk
from tkinter import *

class puntuaciones:
    def __init__(self, idUsuario,engine):
        self.engine=engine
        self.idUsuario=idUsuario
        self.pantallaScore = Tk()
        self.pantallaScore.title("Puntuacion")
        label1 = tk.Label(self.pantallaScore,text="Puntuaciones mas altas", font=("Arial",30)).grid(row=0, columnspan=3)
        # columnas del arbol
        columnas = ('Posicion', 'Tiempo', 'Nombre','Tablero','Fecha')
        # Se crea el arbol de las puntuaciones
        self.listBox = ttk.Treeview(self.pantallaScore, columns=columnas, show='headings')
        # Se establece encabezado de columna
        for col in columnas:
            self.listBox.heading(col, text=col)    
        self.listBox.grid(row=1, column=0, columnspan=2)

        mostrarScores = tk.Button(self.pantallaScore,text="Mostrar Puntuaciones", width=15, command=self.show).grid(row=4, column=0)
        CerrarBtn = tk.Button(self.pantallaScore,text="Atras", width=15, command=self.atras).grid(row=4, column=1)
        self.pantallaScore.mainloop()

    # Mostrar puntuaciones en tabla
    def show(self):
        tempLista = self.engine.obtenerPuntuaciones()

        for i, (Tiempo,Nombre,Tablero,Fecha) in enumerate(tempLista, start=1):
            self.listBox.insert("", "end", values=(i,Tiempo,Nombre,Tablero,Fecha))

    # Salir de la pantalla
    def atras(self):
        self.pantallaScore.destroy()

  
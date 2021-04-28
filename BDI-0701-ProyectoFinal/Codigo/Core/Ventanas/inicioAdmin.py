#-*- coding: utf-8 -*-
from tkinter import *
from Core.Ventanas.puntuaciones import puntuaciones
from Core.Ventanas.Bitacora import Bitacora
from Core.Tableros.sudoku import *
from Core.Ventanas.crearUsuario import crearUsuario

class inicioAdmin:

    def __init__ (self , idUsuario,engine):
        self.idUsuario=idUsuario
        self.engine=engine
        self.pantallaInicio = Tk()
        self.pantallaInicio.geometry("400x400")
        self.pantallaInicio.title("Inicio")
        Label(self.pantallaInicio, text="").pack()
        Button(self.pantallaInicio, text="Reanudar juego", height="2", width="30" , command=self.reanudarJuego).pack()
        Label(self.pantallaInicio, text="").pack()
        Button(self.pantallaInicio, text="Nuevo Juego", height="2", width="30", command=self.nuevoJuego).pack()
        Label(self.pantallaInicio,text="").pack()
        Button(self.pantallaInicio, text="Crear usuario", height="2", width="30",command=self.crear).pack()
        Label(self.pantallaInicio, text="").pack()
        Button(self.pantallaInicio, text="Tabla de Score", height="2", width="30", command=self.tablaScore).pack()
        Label(self.pantallaInicio, text="").pack()
        Button(self.pantallaInicio, text="Bitacora", height="2", width="30", command=self.bitacora).pack()
        Label(self.pantallaInicio, text="").pack()
        self.pantallaInicio.mainloop()

    # Instancia de bitacora
    def bitacora(self):
        Bitacora(self.idUsuario,self.engine)

    # Instancia para crear usuario
    def crear(self ):
        self.pantallaInicio.destroy()
        crearUsuario(self.engine)
       
        

    def reanudarJuego(self):
        ver=self.engine.obtenerUltimoJuego(self.idUsuario)
        if ver:
            newGame=False
            idTablero=self.engine.obtenerIdTablero(self.idUsuario)
            partida=self.engine.obtenerTablero2(idTablero)
            nombre=self.engine.obtenerNombrePartida(self.idUsuario)
            tiempo=self.engine.obtenerTiempo(self.idUsuario)
            game = SudokuGame(ver)
            game.start()
            root = Tk()
            root.resizable(0,0)
            SudokuUI(root, game,newGame,idTablero,ver,self.idUsuario,self.engine)
            root.geometry("%dx%d" % (WIDTH, HEIGHT + 40))
            root.mainloop()
        else:
            tkinter.messagebox.showinfo(message="No hay juego encontrado", title=" Juego no encontrado") 
        self.pantallaInicio.destroy()

    def tablaScore(self):
        puntuaciones(self.idUsuario,self.engine)


    def nuevoJuego(self):
        self.elegirMapa = Tk()
        self.elegirMapa.geometry("400x300")
        self.elegirMapa.title("Inicio")
        Label(self.elegirMapa,text="").pack()
        Button(self.elegirMapa,text="Normal", height="2", width="30", command=self.l33t).pack()
        Label(self.elegirMapa,text="").pack()
        Button(self.elegirMapa,text="Dificil", height="2", width="30", command=self.n00b).pack()
        Label(self.elegirMapa,text="").pack()

    # Tableros disponibles para nuevo juego
    def l33t(self): 
        newGame=True
        partida=self.engine.obtenerNombre(self.idUsuario)
        tablero=self.engine.obtenerTablero2(1)
        idTablero=1
        self.elegirMapa.destroy()
        game=SudokuGame(tablero)
        game.start()
        root = Tk()
        root.resizable(0,0)
        SudokuUI(root, game,newGame,idTablero,partida,self.idUsuario,self.engine)
        root.geometry("%dx%d" % (WIDTH, HEIGHT + 40))
        root.mainloop()
    
    def n00b(self):  
        newGame=True
        partida=self.engine.obtenerNombre(self.idUsuario)
        tablero=self.engine.obtenerTablero2(2)
        idTablero=2
        self.elegirMapa.destroy()
        game=SudokuGame(tablero)
        game.start()
        root = Tk()
        root.resizable(0,0)
        SudokuUI(root, game,newGame,idTablero,partida,self.idUsuario,self.engine)
        root.geometry("%dx%d" % (WIDTH, HEIGHT + 40))
        root.mainloop()

    
        


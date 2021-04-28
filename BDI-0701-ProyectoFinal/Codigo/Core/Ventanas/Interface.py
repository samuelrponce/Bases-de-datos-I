#-*- coding: utf-8 -*-
from Core.Conexion.ConnectionConfig import ConnectionConfig
from Core.Conexion.MySQLEngine import MySQLEngine
from Core.Ventanas.inicioAdmin import inicioAdmin
from Core.Ventanas.inicioUsuario import inicioUsuario
import Core.Tableros
from tkinter import *
import os 
class Interface:
    def __init__(self,engine):
        self.engine = engine
        
        ruta1="/home/roger/Documentos/Proyecto/Codigo/Core/Tableros/l33t.sudoku"
        ruta2="/home/roger/Documentos/Proyecto/Codigo/Core/Tableros/n00b.sudoku"
        ruta3="/home/roger/Documentos/Proyecto/Codigo/Core/Tableros/debug.sudoku"
        ruta4="/home/roger/Documentos/Proyecto/Codigo/Core/Tableros/error.sudoku"
        archivo1=open(ruta1,"r")
        contenidoTabla=archivo1.read()
        archivo2=open(ruta2,"r")
        contenidoTabla=archivo2.read()
        archivo3=open(ruta3,"r")
        contenidoTabla=archivo3.read()
        archivo4=open(ruta4,"r")
        contenidoTabla=archivo4.read()
        self.engine.insertarTablero(1,"debug",contenidoTabla)
        self.engine.insertarTablero(2,"debug",contenidoTabla)
        self.engine.insertarTablero(3,"debug",contenidoTabla)
        self.engine.insertarTablero(4,"debug",contenidoTabla)
        self.pantallaMain()
       
        
    def pantallaMain(self):
        
        global pantallaMain
        pantallaMain =Tk()
        pantallaMain.geometry("400x300")
        pantallaMain.title("Bienvenido")
        Label(text="Bienvenido Usuario", width="300", height="2", font=("Calibri", 13)).pack()
        Label(text="").pack()
        Button(text="Login", height="2", width="30", command = self.login).pack()
        pantallaMain.mainloop()

    def destruirMain():
        pantallaMain.destroy()

    def splash(self):
        self.pantallaSplash = Toplevel(pantallaMain)
        self.pantallaSplash.title("Bienvenido")
        self.pantallaSplash.geometry("300x250")
        Label( text="Bienvenido!", font=18).pack()
        self.pantalla_splash.after(3000) 

    def destruirSplash():

        splash.destroy()
    
    # Diseño de ventana para Login

    def login(self):
        pantallaMain.destroy()
        global pantallaLogin
        self.pantallaLogin = Tk()
        self.pantallaLogin.title("Login")
        self.pantallaLogin.geometry("300x250")
        Label(self.pantallaLogin, text="Ingresar datos para login: ").pack()
        Label(self.pantallaLogin, text="").pack()

        global verificarUsuario
        global verificarContrasenia

        verificarUsuario = StringVar()
        verificarContrasenia = StringVar()

        global entradaUsuarioLogin
        global entradaContraseniaLogin

        Label(self.pantallaLogin, text = "Nombre de Usuario * ").pack()
        entradaUsuarioLogin = Entry(self.pantallaLogin, textvariable = verificarUsuario)
        entradaUsuarioLogin.pack()
        Label(self.pantallaLogin, text = "").pack()
        Label(self.pantallaLogin, text = "Contraseña * ").pack()
        entradaContraseniaLogin = Entry(self.pantallaLogin, textvariable = verificarContrasenia, show= '*')
        entradaContraseniaLogin.pack()
        Label(self.pantallaLogin, text="").pack()
        Button(self.pantallaLogin, text="Login", width=10, height=1 ,command=self.verificarLogin).pack()
       
        

    
    # Verificacion de Login para usuario

    def verificarLogin(self):
        global idUsuario
        usuario1 = verificarUsuario.get()
        contrasenia1 = verificarContrasenia.get()
        entradaUsuarioLogin.delete(0, END)
        entradaContraseniaLogin.delete(0, END)
        idUsuario=self.engine.autenticar(usuario1,contrasenia1)
        if contrasenia1 == self.engine.obtenerPassword(usuario1,contrasenia1):
            self.pantallaLogin.destroy()
            self.loginSuccess()
            
        else:
            self.ContraseniaNoReconocida()

    # Diseño popup para aceptacion de login
    def loginSuccess(self):
        global pLoginSuccess
        pLoginSuccess = Tk()
        pLoginSuccess.title("Satisfactorio!")
        pLoginSuccess.geometry("300x100")
        Label(pLoginSuccess, text="Inicio Satisfactorio!").pack()
        Button(pLoginSuccess, text="OK", command=self.EliminarLoginSuccess).pack()

    # Diseño popup para login invalido de constrasenia
    def ContraseniaNoReconocida(self):
        global pContraseniaNoRe
        pContraseniaNoRe = Tk()
        pContraseniaNoRe.title("Satisfactorio")
        pContraseniaNoRe.geometry("300x100")
        Label(pContraseniaNoRe, text="Contraseña invalida").pack()
        Button(pContraseniaNoRe, text="OK", command=self.eliminarContraseniaNoRe).pack()


    # Eliminacion de ventanas popup
    def EliminarLoginSuccess(self):
        pLoginSuccess.destroy()
        if idUsuario == 1:
            inicioAdmin(idUsuario,self.engine)
        else:
            inicioUsuario(idUsuario,self.engine)
        

    # Eliminacion de ventana pop up para una contrasenia sin reconocer
    def eliminarContraseniaNoRe(self):
        pContraseniaNoRe.destroy()



        

    



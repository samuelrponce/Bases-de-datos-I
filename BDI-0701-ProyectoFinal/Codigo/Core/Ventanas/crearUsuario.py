#-*- coding: utf-8 -*-
from tkinter import *
import tkinter as tk
from tkinter import ttk


class crearUsuario:
    def __init__(self,engine):
        self.engine = engine
        self.crear_user()

    def crear_user(self):
        global pantallaUser
        pantallaUser = Tk()
        #self.pantallaUser = Toplevel(self.pantallaUser)
        pantallaUser.title("Crear Usuario")
        pantallaUser.geometry("500x500")

        Label(pantallaUser, text="Ingrese datos para un nuevo usuario: ").pack()
        Label(pantallaUser, text="").pack()

        global verificarUsuario
        global verificarContrasenia

        verificarUsuario = StringVar()
        verificarContrasenia = StringVar()
      

        global entradaUsuario
        global entradaContrasenia
    

        Label(pantallaUser, text = "Nombre de Usuario: ").pack()
        entradaUsuario = Entry(pantallaUser, textvariable = verificarUsuario)
        entradaUsuario.pack()
        Label(pantallaUser, text = "").pack()
        Label(pantallaUser, text = "Contraseña: ").pack()
        entradaContrasenia = Entry(pantallaUser, textvariable=verificarContrasenia ,show='*')
        entradaContrasenia.pack()
        Label(pantallaUser, text="").pack()
        Button(pantallaUser, text="Crear Usuario", width=20, height=1 ,command=self.crear).pack()
        Label(pantallaUser, text="").pack()
        Button(pantallaUser, text="Eliminar Usuario", width=20, height=1, command=self.eliminarUsuario ).pack()
        Label(pantallaUser, text="").pack()
        Button(pantallaUser, text="Actualizar Usuario", width=20, height=1,command=self.modificarUsuario ).pack()
        pantallaUser.mainloop()

    def crear(self):
        usuario1=verificarUsuario.get()
        contrasenia1=verificarContrasenia.get()
        existe = self.engine.crearUsuario(usuario1,contrasenia1)
        if not existe:
            self.usuarioIngresado()
        else:
             self.usuarioExistente()

    def eliminarUsuario(self):
        usuario1=verificarUsuario.get()
        contrasenia1=verificarContrasenia.get()
        idUsuario=self.engine.autenticar(usuario1,contrasenia1)
        if idUsuario:
            self.engine.eliminarUsuario(idUsuario)
            self.usuarioEliminado() 
        else:
            self.usuarioNoEncontrado()
    
    def modificarUsuario(self):
        pantallaUser.destroy()
        self.pantallaUsuarios = Tk()
        self.pantallaUsuarios.title("Usuarios registrados")
         
        self.pantallaUsuarios.geometry("500x500")

        Label(self.pantallaUsuarios, text="Actualizar usuario por el ID: ").pack()
        Label(self.pantallaUsuarios, text="").pack()

        global verificarID
        global verificarUsuario
        global verificarContrasenia

        verificarID =StringVar()
        verificarUsuario = StringVar()
        verificarContrasenia = StringVar()
      
        global entradaID
        global entradaUsuario
        global entradaContrasenia
    

        Label(self.pantallaUsuarios, text = "ID de Usuario: ").pack()
        entradaID = Entry(self.pantallaUsuarios, textvariable = verificarID)
        entradaID.pack()
        Label(self.pantallaUsuarios, text  = "").pack()
        Label(self.pantallaUsuarios, text = "Nombre de Usuario: ").pack()
        entradaUsuario = Entry(self.pantallaUsuarios, textvariable = verificarUsuario)
        entradaUsuario.pack()
        Label(self.pantallaUsuarios, text = "").pack()
        Label(self.pantallaUsuarios, text = "Contraseña: ").pack()
        entradaContrasenia = Entry(self.pantallaUsuarios, textvariable=verificarContrasenia ,show='*')
        entradaContrasenia.pack()
        Label(self.pantallaUsuarios, text="").pack()
        Button(self.pantallaUsuarios, text="Buscar Usuario", width=20, height=1 ,command=self.Buscar).pack()
        Label(self.pantallaUsuarios, text="").pack()
        Button(self.pantallaUsuarios, text="Actualizar Usuario", width=20, height=1,command=self.Actualizar ).pack()
        self.pantallaUsuarios.mainloop()

    def Buscar(self):
        ID = verificarID.get()
        nombre = self.engine.obtenerNombre(ID)
        Contra = self.engine.obtenerContra(ID)
        entradaID.delete(0,END)
        entradaID.insert(0,ID)
        entradaUsuario.insert(0,nombre)
        entradaContrasenia.insert(0,Contra)

    def Actualizar(self):
        ID = verificarID.get()
        nombre = verificarUsuario.get()
        Contra = verificarContrasenia.get()
        entradaID.delete(0,END)
        entradaUsuario.delete(0,END)
        entradaContrasenia.delete(0,END)
        self.engine.modificarUsuario(ID,nombre,Contra)
        self.pantallaUsuarios.destroy()


    # Ventana para eliminar usuario
    def usuarioEliminado(self):
        global usuarioEliminad
        usuarioEliminad = Tk()
        usuarioEliminad.title("Realizado")
        usuarioEliminad.geometry("300x100")
        Label(usuarioEliminad,text=" Usuario ha sido eliminado").pack()
        Button(usuarioEliminad,text="OK",command = self.ok2).pack()

    def usuarioNoEncontrado(self):
        global usuarioNoEncontrad
        usuarioNoEncontrad = Tk()
        usuarioNoEncontrad.title("No encontrado!")
        usuarioNoEncontrad.geometry("300x100")
        Label(usuarioNoEncontrad,text=" Usuario no ha sido encontrado").pack()
        Button(usuarioNoEncontrad,text="OK",command = self.ok).pack()
    
    # Eliminar ventanas al buscar usuario
    def ok(self):
        usuarioNoEncontrad.destroy()
        entradaUsuario.delete(0, END)
        entradaContrasenia.delete(0, END)

    # Eliminar ventanas al eliminar usuario
    def ok2(self):
        usuarioEliminad.destroy()
        entradaUsuario.delete(0, END)
        entradaContrasenia.delete(0, END)

    def usuarioIngresado(self):
        global usuarioCreado
        usuarioCreado = Tk()
        usuarioCreado.title("Exito")
        usuarioCreado.geometry("300x100")
        Label(usuarioCreado, text="El usuario ha sido ingresado").pack()
        Button(usuarioCreado, text="OK", command = self.aceptar2).pack()
        

    # Verificacion de existencia de usuario
    def usuarioExistente(self):
        
        global usuarioExiste
        usuarioExiste = Tk()
        usuarioExiste.title("Invalido")
        usuarioExiste.geometry("300x100")
        Label(usuarioExiste, text="El usuario ya existe").pack()
        Button(usuarioExiste, text="OK", command = self.aceptar).pack()
        

    # Aceptar usuario creado
    def aceptar2(self):
        usuarioCreado.destroy()
        entradaUsuario.delete(0, END)
        entradaContrasenia.delete(0, END)

    # Aceptar usuario existente
    def aceptar(self):
        usuarioExiste.destroy() 
        entradaUsuario.delete(0, END)
        entradaContrasenia.delete(0, END)

    # Eliminar ventana de contraseña no reconocida
    def eliminarContraseniaNoRe(self):
        pContraseniaNoRe.destroy()



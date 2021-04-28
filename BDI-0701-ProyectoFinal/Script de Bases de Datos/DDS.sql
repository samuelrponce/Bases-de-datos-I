
DROP DATABASE IF EXISTS BaseDeDatos1;

CREATE DATABASE BaseDeDatos1 CHARACTER SET utf8;

USE BaseDeDatos1;

DROP TABLE IF EXISTS Rol;
DROP TABLE IF EXISTS Cuenta;
DROP TABLE IF EXISTS Puntuaciones;
DROP TABLE IF EXISTS Bitacora;
DROP TABLE IF EXISTS PartidaEspera;
DROP TABLE IF EXISTS Tableros;

CREATE TABLE Rol(
    id INT PRIMARY KEY AUTO_INCREMENT NOT NULL COMMENT "id auto incremental" ,
    txt_nombreRol TEXT NOT NULL COMMENT "nombre de rol" 
) COMMENT "tabla de roles";

INSERT INTO Rol (txt_nombreRol) VALUES
("ADMIN"),("USUARIO") ;

CREATE TABLE Cuenta(
    id INT PRIMARY KEY AUTO_INCREMENT NOT NULL COMMENT "id auto incremental",
    txt_nombre TEXT NOT NULL COMMENT "nombre de usuario",
    txt_password TEXT NOT NULL COMMENT "contrasenia de la cuenta",
    id_rol INT NOT NULL DEFAULT 2 COMMENT "id de rol",
    CONSTRAINT fk_rol_id FOREIGN KEY (id_rol) REFERENCES Rol(id) ON DELETE CASCADE
) COMMENT "Tabla de usuarios";

INSERT INTO Cuenta(id,txt_nombre,txt_password,id_rol) VALUES(1,"Roger",1234,1);
INSERT INTO Cuenta(txt_nombre,txt_password) VALUES("Rene","Rene");
INSERT INTO Cuenta(txt_nombre,txt_password) VALUES("Estefania","Estefania");


CREATE TABLE Tableros(
    id INT PRIMARY KEY AUTO_INCREMENT NOT NULL COMMENT "id auto incremental",
    txt_fileName TEXT NOT NULL COMMENT "nombre de tablero",
    jso_partida LONGTEXT COMMENT "Tipos de Tableros"
  ) COMMENT "Tabla de Tableros disponibles";

CREATE TABLE Puntuaciones(
    id INT PRIMARY KEY AUTO_INCREMENT NOT NULL COMMENT "id auto incremental",
    txt_partida TEXT NOT NULL COMMENT "Nombre de partida",
    int_tiempo INT NOT NULL COMMENT "Tiempo de partida",
    dat_fecha TIMESTAMP NOT NULL DEFAULT NOW() COMMENT "fecha de la partida",
    id_cuenta INT COMMENT "id de la cuenta",
    id_tablero INT COMMENT "id del tablero",
    CONSTRAINT fk_Cuenta_id FOREIGN KEY (id_cuenta) REFERENCES Cuenta(id) ON DELETE CASCADE ,
    CONSTRAINT fk_tablero_id FOREIGN KEY (id_tablero) REFERENCES Tableros (id) ON DELETE CASCADE 
) COMMENT "Tabla de puntuaciones";

CREATE TABLE PartidaEspera(
    id INT PRIMARY KEY AUTO_INCREMENT NOT NULL COMMENT "id auto incremental",
    txt_partida TEXT NOT NULL COMMENT "nombre de la partida",
    dat_fecha TIMESTAMP NOT NULL DEFAULT NOW() COMMENT "fecha de la partida",
    int_tiempo INT NOT NULL COMMENT "tiempo de la partida", 
    id_cuenta INT COMMENT "id de la cuenta",
    jso_partida JSON NOT NULL COMMENT "contenido de la partida",
    id_tablero INT COMMENT "id del tablero",
    CONSTRAINT fk_cuentas_id FOREIGN KEY (id_cuenta) REFERENCES Cuenta(id) ON DELETE CASCADE,
    CONSTRAINT fk_tableros_id FOREIGN KEY (id_tablero) REFERENCES Tableros(id) ON DELETE CASCADE
) COMMENT "Tabla de partidas guardadas automaticamente";



CREATE TABLE Bitacora (
  id INT PRIMARY KEY AUTO_INCREMENT NOT NULL COMMENT "id auto incremental",
  id_cuenta INT NOT NULL COMMENT "id de usuario", 
  txt_accion TEXT NOT NULL COMMENT "accion que realizo",
  dat_fecha DATETIME NOT NULL DEFAULT NOW() COMMENT "fecha en la que realizo la accion"
) COMMENT "Tabla de bitacora";


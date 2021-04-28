USE BaseDeDatos1;

DROP PROCEDURE IF EXISTS sp_actualizarJuego;
DROP PROCEDURE IF EXISTS sp_autenticar;
DROP PROCEDURE IF EXISTS sp_crearUsuario;
DROP PROCEDURE IF EXISTS sp_eliminarJuego;
DROP PROCEDURE IF EXISTS sp_eliminarUsuario;
DROP PROCEDURE IF EXISTS sp_guardarPuntuacion;
DROP PROCEDURE IF EXISTS sp_iniciarJuego;
DROP PROCEDURE IF EXISTS sp_modificarUsuario;
DROP PROCEDURE IF EXISTS sp_obtenerNombrePartida;
DROP PROCEDURE IF EXISTS sp_obtenerPassword;
DROP PROCEDURE IF EXISTS sp_obtenerRol;
DROP PROCEDURE IF EXISTS sp_obtenerTablero;
DROP PROCEDURE IF EXISTS sp_obtenerTablero2;
DROP PROCEDURE IF EXISTS sp_obtenerTiempo;
DROP PROCEDURE IF EXISTS sp_obtenerUltimoJuego;
DROP PROCEDURE IF EXISTS sp_obtenerIdTablero;
DROP PROCEDURE IF EXISTS sp_insertarTableros;
DROP PROCEDURE IF EXISTS sp_obtenerNombre;
DROP PROCEDURE IF EXISTS sp_obtenerPassword2;




delimiter $$
/*sp_obtenerPassword2*/
CREATE PROCEDURE sp_obtenerPassword2 (IN idUsuario TEXT, OUT contra TEXT)
       BEGIN
         SELECT Cuenta.txt_password INTO contra FROM Cuenta
         WHERE  Cuenta.id = idUsuario ;

       END$$ 

/*sp_obtenerNombre*/
CREATE PROCEDURE sp_obtenerNombre (IN idUsuario TEXT, OUT nombre TEXT)
       BEGIN
         SELECT Cuenta.txt_nombre INTO nombre FROM Cuenta
         WHERE  Cuenta.id = idUsuario ;

       END$$ 


/*sp_obtenerIdTablero*/
CREATE PROCEDURE sp_obtenerIdTablero (IN idUsuario TEXT, OUT idTablero INT)
       BEGIN
         SELECT PartidaEspera.id_tablero INTO idTablero FROM PartidaEspera
         WHERE  PartidaEspera.id_cuenta = idUsuario ;

       END$$ 

/*sp_obtenerPassword*/
CREATE PROCEDURE sp_obtenerPassword (IN nombre TEXT,IN Cpassword TEXT, OUT Vpassword TEXT)
       BEGIN
         SELECT Cuenta.txt_password INTO Vpassword FROM Cuenta
         WHERE (BINARY Cuenta.txt_nombre = nombre ) AND ( BINARY Cuenta.txt_password = Cpassword );

       END$$ 

/*sp_autenticar */

CREATE PROCEDURE sp_autenticar (IN nombre TEXT,IN Cpassword TEXT, OUT idUsuario INT)
       BEGIN
         SELECT Cuenta.id INTO idUsuario FROM Cuenta
         WHERE (BINARY Cuenta.txt_nombre = nombre ) AND ( BINARY Cuenta.txt_password = Cpassword );

         IF idUsuario IS NOT NULL THEN
            INSERT INTO Bitacora(id_cuenta, txt_accion, dat_fecha) VALUES(
                idUsuario,
                'AUTENTICACION',
                NOW()
              );
              COMMIT;
          END IF;
         END$$


/*sp_obtenerRol*/

CREATE PROCEDURE sp_obtenerRol (IN nombre TEXT,IN Cpassword TEXT, OUT datos TEXT)
       BEGIN
         SELECT Rol.txt_nombreRol INTO datos FROM Cuenta JOIN Rol ON Cuenta.id_rol = Rol.id
         WHERE (BINARY Cuenta.txt_nombre = nombre) AND (BINARY Cuenta.txt_password = Cpassword) ;
       END$$

/*sp_obtenerUltimoJuego*/

CREATE PROCEDURE sp_obtenerUltimoJuego ( IN idUsuario INT, OUT jsonPartida JSON)
      BEGIN
        SELECT PartidaEspera.jso_partida INTO jsonPartida FROM PartidaEspera WHERE PartidaEspera.id_cuenta= idUsuario ;        
          INSERT INTO Bitacora(id_cuenta, txt_accion, dat_fecha) VALUES(
                idUsuario,
                "REANUDAR JUEGO",
                NOW()
              );
          COMMIT;
      END$$
  
/* sp_obtenerTablero*/

CREATE PROCEDURE sp_obtenerTablero ( IN idUsuario INT,OUT jsonTablero JSON)
      BEGIN
        SELECT Tableros.jso_partida INTO jsonTablero FROM PartidaEspera  
        INNER JOIN Tableros        
        ON PartidaEspera.id_tablero=Tableros.id
        WHERE PartidaEspera.id_cuenta= idUsuario;
      END$$
    
/* sp_obtenerTablero2*/

CREATE PROCEDURE sp_obtenerTablero2 ( IN idTablero INT,OUT jsonTablero JSON)
      BEGIN
        SELECT Tableros.jso_partida INTO jsonTablero FROM Tableros  WHERE Tableros.id= idTablero;
      END$$

/* sp_obtenerTiempo*/

CREATE PROCEDURE sp_obtenerTiempo ( IN idUsuario INT,OUT tiempo INT)
      BEGIN
        SELECT PartidaEspera.int_tiempo INTO tiempo FROM PartidaEspera WHERE PartidaEspera.id_cuenta= idUsuario;
      END$$

/*sp_obtenerNombrePartida*/

CREATE PROCEDURE sp_obtenerNombrePartida ( IN idUsuario INT,OUT nombrePartida TEXT)
      BEGIN
        SELECT PartidaEspera.txt_partida INTO nombrePartida FROM PartidaEspera WHERE PartidaEspera.id_cuenta= idUsuario;
      END$$

/*sp_actualizarJuego*/
 
CREATE PROCEDURE sp_actualizarJuego (IN idUsuario INT, IN tiempo INT, IN jsonPartida JSON )
      BEGIN
        
        
        UPDATE PartidaEspera SET
          jso_partida = jsonPartida,
          int_tiempo = tiempo
        WHERE
          id_cuenta = idUsuario;

        COMMIT;
        
      END$$

/*sp_eliminarJuego*/
 
CREATE PROCEDURE sp_eliminarJuego (IN partidaId INT)
      BEGIN
        
        DECLARE existe INT;

        SELECT PartidaEspera.id INTO existe FROM PartidaEspera WHERE BINARY partidaId = PartidaEspera.id;
        
        IF existe IS NOT NULL THEN
          DELETE FROM PartidaEspera
          WHERE PartidaEspera.id = partidaId;
          COMMIT;
        END IF;
        
      END$$

/*sp_iniciarJuego*/
CREATE PROCEDURE sp_iniciarJuego(IN idTablero INT, IN tiempo INT, IN nombrePartida TEXT, IN idUsuario INT, IN jsonPartida JSON)
      BEGIN

        DECLARE existe INT;
        SELECT PartidaEspera.id INTO existe FROM PartidaEspera 
        WHERE (BINARY PartidaEspera.txt_partida = nombrePartida) AND (PartidaEspera.id_cuenta = idUsuario);

        IF existe IS NOT NULL THEN
          DELETE FROM PartidaEspera WHERE PartidaEspera.id_cuenta=idUsuario;

          INSERT INTO Bitacora(id_cuenta, txt_accion, dat_fecha) VALUES(
                idUsuario,
                "INICIAR JUEGO",
                NOW()
              );
          SELECT PartidaEspera.id INTO existe FROM PartidaEspera WHERE (BINARY PartidaEspera.txt_partida = nombrePartida) AND (PartidaEspera.id_cuenta = idUsuario);
          COMMIT;
        END IF;
        INSERT INTO PartidaEspera(txt_partida,int_tiempo,id_cuenta,jso_partida,id_tablero) VALUES(
          nombrePartida,
          tiempo,
          idUsuario,
          jsonPartida,
          idTablero
        );
        COMMIT;

      END$$

/*sp_crearUsuario */
CREATE PROCEDURE sp_crearUsuario (IN nombre TEXT, IN Cpassword TEXT, OUT valido INT)
      BEGIN
        SELECT Cuenta.id INTO valido FROM Cuenta WHERE (Cuenta.txt_nombre = nombre );

        IF valido IS NULL THEN
          INSERT INTO Cuenta(txt_nombre, txt_password) 
          VALUES
          (
            nombre,
            Cpassword
          );
          COMMIT;
        END IF;

      END$$

/*sp_modificarUsuario*/
CREATE PROCEDURE sp_modificarUsuario (IN idUsuario INT, IN nombre TEXT, IN Cpassword TEXT)
  BEGIN
    UPDATE Cuenta SET
      txt_nombre = nombre,
      txt_password = Cpassword
    WHERE id = idUsuario;

    COMMIT;   
  END$$

/*sp_eliminarUsuario*/
CREATE PROCEDURE sp_eliminarUsuario (IN idUsuario INT)
      BEGIN
        DECLARE verificar INT;

        SELECT Cuenta.id INTO verificar FROM Cuenta WHERE BINARY idUsuario = Cuenta.id;
        
        IF verificar IS NOT NULL THEN
          DELETE FROM Cuenta
          WHERE Cuenta.id = idUsuario;

          COMMIT;
        END IF;    
      END$$

/*sp_guardarPuntuacion*/
CREATE PROCEDURE sp_guardarPuntuacion ( IN nombrePartida TEXT, IN tiempo INT, IN idCuenta INT, IN idTablero INT )
     BEGIN
        INSERT INTO Puntuaciones (txt_partida, int_tiempo, id_cuenta, id_tablero,dat_fecha) VALUES (
          nombrePartida,
          tiempo,
          idCuenta,
          idTablero,
          NOW()
        );
        COMMIT;
        INSERT INTO Bitacora(id_cuenta, txt_accion, dat_fecha) VALUES(
              idCuenta,
              "PUNTAJE",
              NOW()
            );
        COMMIT;
      END$$

/*sp_insertarTableros*/
CREATE PROCEDURE sp_insertarTableros (IN id INT, IN nombreTablero TEXT, IN archivo JSON)
     BEGIN
        INSERT INTO Tableros(id,txt_fileName,jso_partida) VALUES(id,nombreTablero,archivo);
        COMMIT;
      END$$
delimiter ;
      
SELECT  ROUTINE_CATALOG, ROUTINE_SCHEMA, ROUTINE_NAME, ROUTINE_TYPE  FROM INFORMATION_SCHEMA.ROUTINES
  WHERE ROUTINE_TYPE = 'PROCEDURE';


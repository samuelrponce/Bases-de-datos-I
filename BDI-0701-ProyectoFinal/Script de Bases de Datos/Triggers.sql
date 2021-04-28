USE BaseDeDatos1;

DELIMITER $$
   
    DROP TRIGGER IF EXISTS tr_agregarUsuario$$
    DROP TRIGGER IF EXISTS tr_editarUsuario$$
    DROP TRIGGER IF EXISTS tr_eliminarUsuario$$
    DROP TRIGGER IF EXISTS tr_iniciarJuego$$
    DROP TRIGGER IF EXISTS tr_actualizarJuego$$
    DROP TRIGGER IF EXISTS tr_reanudarJuego$$
    DROP TRIGGER IF EXISTS tr_encriptarCuenta$$

    CREATE TRIGGER tr_agregarUsuario 
    AFTER INSERT 
    ON Cuenta FOR EACH ROW
    BEGIN
        INSERT INTO Bitacora(id_cuenta, txt_accion, dat_fecha) VALUES(
            1, 
            "CUENTA CREADA",
            NOW()
        ); 
    END$$
       
    CREATE TRIGGER tr_editarUsuario 
    AFTER UPDATE 
    ON Cuenta FOR EACH ROW
    BEGIN
        INSERT INTO Bitacora(id_cuenta, txt_accion, dat_fecha) VALUES(
            1, 
            "CUENTA MODIFICADA",
            NOW()
        );    
    END$$
    
    CREATE TRIGGER tr_eliminarUsuario 
    BEFORE DELETE 
    ON Cuenta FOR EACH ROW
    BEGIN
        INSERT INTO Bitacora(id_cuenta, txt_accion, dat_fecha) VALUES(
            1, 
            "CUENTA ELIMINADA",
            NOW()
        ); 
    END$$

    CREATE TRIGGER tr_iniciarJuego 
    AFTER INSERT 
    ON PartidaEspera FOR EACH ROW
    BEGIN
        INSERT INTO Bitacora(id_cuenta, txt_accion, dat_fecha) VALUES(
            NEW.id_cuenta, 
            "JUEGO INICIADO",
            NOW()
        ); 
    END$$
    
    CREATE TRIGGER tr_actualizarJuego 
    AFTER UPDATE 
    ON PartidaEspera FOR EACH ROW
    BEGIN
        

    END$$
    
    CREATE TRIGGER tr_reanudarJuego 
    BEFORE UPDATE 
    ON PartidaEspera FOR EACH ROW
        BEGIN
            INSERT INTO Bitacora(id_cuenta, txt_accion, dat_fecha) VALUES(
                NEW.id_cuenta, 
                "JUEGO INICIADO",
                NOW()
            ); 
        END$$
    
    CREATE TRIGGER tr_encriptarCuenta 
    BEFORE INSERT  
    ON Cuenta FOR EACH ROW
    BEGIN
        SET NEW.txt_nombre = NEW.txt_nombre;
        SET NEW.txt_password = NEW.txt_password;
    END$$



DELIMITER ;
USE BaseDeDatos1

DROP VIEW IF EXISTS Usuarios;

CREATE VIEW Usuarios AS
    SELECT
        id,
        txt_nombre,
        txt_password
    FROM
        Cuenta
    WHERE
        id_rol = 2
    ORDER BY
        id ASC
;

DROP VIEW IF EXISTS TopPuntuaciones;

CREATE VIEW TopPuntuaciones AS
    SELECT 
        int_tiempo,
        Cuenta.txt_nombre,
        Tableros.id,
        dat_fecha
    FROM 
        Puntuaciones
    INNER JOIN
        Cuenta
    ON 
        Puntuaciones.id_cuenta=Cuenta.id
    INNER JOIN
        Tableros        
    ON 
        Puntuaciones.id_tablero=Tableros.id
    WHERE
        int_tiempo < 200
    ORDER BY
        int_tiempo ASC
;

DROP VIEW IF EXISTS RegistroBitacora;

CREATE VIEW RegistroBitacora AS
    SELECT 
        Bitacora.id,
        Cuenta.txt_nombre,
        Bitacora.txt_accion,
        Bitacora.dat_fecha
    FROM 
        Bitacora
    INNER JOIN
        Cuenta
    ON 
        Bitacora.id_cuenta=Cuenta.id
    ORDER BY
        dat_fecha ASC
;


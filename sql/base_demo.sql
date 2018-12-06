CREATE DATABASE base_yaz;

USE base_yaz;

CREATE TABLE datos(
    email varchar(50) NOT NULL PRIMARY KEY,
    nombre varchar(50) NOT NULL,
    apellidos varchar(100) NOT NULL,
    telefono varchar(20) NOT NULL,
    password varchar(32) NOT NULL
)ENGINE=InnoDB DEFAULT CHARSET=latin1;


INSERT INTO datos (email, nombre, apellidos, telefono, password)
VALUES ('dejah@email', 'Jose', 'Hernandez Mendoza', '5518301849','1234'),('jhon@email', 'Adriana', 'Rivera Pacheco','5501581749','5678');

SHOW TABLES;

SELECT * FROM datos;

DESCRIBE datos;

SELECT "Creando un usuario y asignandolo a la base de datos" as "Mensaje";
CREATE USER 'unid'@'localhost' IDENTIFIED BY 'unid.2018';
GRANT ALL PRIVILEGES ON base_demo.* TO 'kuorra'@'localhost';
GRANT ALL PRIVILEGES ON base_demo.* TO kuorra@'%' IDENTIFIED BY 'kuorra.remote';

FLUSH PRIVILEGES;
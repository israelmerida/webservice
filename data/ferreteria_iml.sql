CREATE DATABASE ferreteria_iml;

USE ferreteria_iml;


 create table cliente (
      id_cliente int null auto_increment primary key,
      nombre varchar(20) not null,
      apellido_paterno varchar(30) not null,
      apellido_materno  varchar(30) not null,
      telefono char(10) not null,
      email varchar(50) not null
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=latin1 COLLATE=latin1_spanish_ci;


insert into cliente (id_cliente,nombre,apellido_paterno,apellido_materno,telefono,email)values
     (1,'Alexis','Perez','Salas','7751235689','alexis@hotmail.com'),
     (2,'Diego','Lopez','Lopez','7756456890','diego@gmail.com'),
     (3,'Carlos','Merida','Lopez','7752134560','carlos@hotmail.com');



create database holamundo2;
show databases;
use holamundo2;
CREATE TABLE animales (
    id INT,
    tipo VARCHAR(255),
    estado VARCHAR(255),
    PRIMARY KEY (id)
);
ALTER table animales modify column id int auto_increment;
insert into animales (tipo, estado) values ("chanchito","Feliz");
-- Poner comentarios... con dos lineas medias.
select * from animales;


Create Database JuegoRPG;

use JuegoRPG;

CREATE TABLE Personaje (
    idPersonaje INT AUTO_INCREMENT PRIMARY KEY,
    Nombre VARCHAR(50),
    clase VARCHAR(50),
    nivel INT,
    ataque float,
    defensa float,
    vida float
);

CREATE TABLE Inventario (
    idItem INT AUTO_INCREMENT PRIMARY KEY,
    nombreItem VARCHAR(50),
    bonus float,
    idPersonaje INT,
    FOREIGN KEY (idPersonaje) REFERENCES Personaje(idPersonaje) ON DELETE CASCADE
);

INSERT INTO Personaje (Nombre, clase, nivel, ataque, defensa, vida) 
VALUES ('Aragorn', 'Guerrero', 10, 50.0, 30.0, 100.0);
INSERT INTO Personaje (Nombre, clase, nivel, ataque, defensa, vida) 
VALUES ('Gandalf', 'Mago', 12, 60.0, 10.0, 80.0);
INSERT INTO Personaje (Nombre, clase, nivel, ataque, defensa, vida) 
VALUES ('Legolas', 'Arquero', 11, 55.0, 20.0, 90.0);

INSERT INTO Inventario (nombreItem, bonus) 
VALUES ('Escudo', '15');
INSERT INTO Inventario (nombreItem, bonus) 
VALUES ('Cuchillo', '4');
INSERT INTO Inventario (nombreItem, bonus) 
VALUES ('Collar', '40');
INSERT INTO Inventario (nombreItem, bonus) 
VALUES ('Orbe', '12');
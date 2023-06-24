CREATE TABLE Comuna (
  id_comuna INT PRIMARY KEY,
  pais VARCHAR(50),
  region VARCHAR(50),
  nombre_comuna VARCHAR(100),
  poblacion INT,
  superficie FLOAT
);

CREATE TABLE Entretencion (
  id_entretencion INT PRIMARY KEY,
  id_comuna INT,
  categoria_entretencion VARCHAR(50),
  nombre_entretencion VARCHAR(100),
  ubicacion_entretencion VARCHAR(200),
  FOREIGN KEY (id_comuna) REFERENCES Comuna(id_comuna)
);

CREATE TABLE Educacion (
  id_institucion INT PRIMARY KEY,
  id_comuna INT,
  nombre_institucion VARCHAR(200),
  nivel VARCHAR(50),
  afiliacion_institucion VARCHAR(100),
  FOREIGN KEY (id_comuna) REFERENCES Comuna(id_comuna)
);


CREATE TABLE Panorama_laboral (
  id_panorama INT PRIMARY KEY,
  id_comuna INT,
  pob_edad_trabajar INT,
  hom_edad_trabajar INT,
  muj_edad_trabajar INT,
  hom_ocupados INT,
  muj_ocupadas INT,
  FOREIGN KEY (id_comuna) REFERENCES Comuna(id_comuna)
);


CREATE TABLE Centros_Salud (
  id_centro INT PRIMARY KEY,
  id_comuna INT,
  nombre_centro VARCHAR(100),
  tipo_centro VARCHAR(50),
  afiliacion_centro VARCHAR(50),
  FOREIGN KEY (id_comuna) REFERENCES Comuna(id_comuna)
);


CREATE TABLE Indicadores (
  nombre_indicador VARCHAR(100) PRIMARY KEY,
  tema VARCHAR(100)
);

CREATE TABLE Tiene_indicadores (
  id_comuna INT,
  nombre_indicador VARCHAR(100),
  cantidad INT,
  valor FLOAT,
  desempeño VARCHAR(50),
  PRIMARY KEY (id_comuna, nombre_indicador),
  FOREIGN KEY (id_comuna) REFERENCES Comuna(id_comuna),
  FOREIGN KEY (nombre_indicador) REFERENCES Indicadores(nombre_indicador)
);

CREATE DATABASE Información_territorial_basada_en_las_comunas_de_Chile;

USE Información_territorial_basada_en_las_comunas_de_Chile;

CREATE TABLE Pais (
    id_pais INT PRIMARY KEY,
    nombre_pais VARCHAR(255)
);

CREATE TABLE Region (
    id_region INT PRIMARY KEY,
    id_pais INT,
    nombre_region VARCHAR(255),
    FOREIGN KEY (id_pais) REFERENCES Pais(id_pais)
);

CREATE TABLE Comuna (
    id_comuna INT PRIMARY KEY,
    id_region INT,
    nombre_comuna VARCHAR(255),
    poblacion INT,
    FOREIGN KEY (id_region) REFERENCES Region(id_region)
);

CREATE TABLE Entretencion (
    id_entretencion INT PRIMARY KEY,
    id_comuna INT,
    categoria_entretencion VARCHAR(255),
    nombre_entretencion VARCHAR(255),
    ubicacion_entretencion VARCHAR(255),
    FOREIGN KEY (id_comuna) REFERENCES Comuna(id_comuna)
);

CREATE TABLE Educacion (
    id_institucion INT PRIMARY KEY,
    id_comuna INT,
    nombre_institucion VARCHAR(255),
    nivel VARCHAR(255),
    afiliacion_institucion VARCHAR(255),
    FOREIGN KEY (id_comuna) REFERENCES Comuna(id_comuna)
);

CREATE TABLE Panorama_Laboral (
    id_panorama INT PRIMARY KEY,
    id_comuna INT,
    pob_edad_trabajar INT,
    hom_edad_trabajar INT,
    muj_edad_trabajar INT,
    hom_ocupados INT,
    muj_ocupadas INT,
    FOREIGN KEY (id_comuna) REFERENCES Comuna(id_comuna)
);

CREATE TABLE Centros_de_salud (
    id_centro INT PRIMARY KEY,
    id_comuna INT,
    nombre_centro VARCHAR(255),
    tipo_centro VARCHAR(255),
    afiliacion_centro VARCHAR(255),
    FOREIGN KEY (id_comuna) REFERENCES Comuna(id_comuna)
);

CREATE TABLE Indicadores (
    id_comuna INT,
    ind_entretencion VARCHAR(100),
    ind_educacion VARCHAR(100),
    ind_laboral VARCHAR(100),
    ind_salud VARCHAR(100),
    ind_total VARCHAR(100),
    FOREIGN KEY (id_comuna) REFERENCES Comuna(id_comuna)
);

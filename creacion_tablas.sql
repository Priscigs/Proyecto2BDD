/* Universidad del Valle de Guatemala
   Base de Datos 1
   Proyecto # 2
   Priscilla González Sandoval - 20689
   Estefanía Elvira - 20725
   Elean Rivas - 19062 */

-- CREACIÓN DE TABLAS EN POSTGRESQL

--DDL
CREATE TABLE 
	peliculas(duracion INT,
			  id_pelicula VARCHAR(10),
			  titulo VARCHAR(100),
			  fecha_lanzamiento DATE,
			  director VARCHAR(50),
			  clasificacion VARCHAR(5),
			  PRIMARY KEY (id_pelicula));
		
CREATE TABLE 
	actores(nombre VARCHAR(50),
			edad INT,
			fecha_nac DATE,
			pais_origen VARCHAR(100), 
			id_actor VARCHAR(10),
			PRIMARY KEY (id_actor));

CREATE TABLE 
	director(nombre VARCHAR(50),
			 edad INT,
			 fecha_nac DATE,
			 pais_origen VARCHAR(100),
			 id_director VARCHAR(10),
			 PRIMARY KEY(id_director));
			 
CREATE TABLE 
	productora(nombre VARCHAR(50),
			   pais VARCHAR(100),
			   presupuesto FLOAT,
			   c_empleados INT,
			   PRIMARY KEY (nombre));

CREATE TABLE 
	sponsor(nombre VARCHAR(50),
		    tipo_contrato VARCHAR (50),
		    id_sponsor VARCHAR (10),
		    PRIMARY KEY (id_sponsor));
		   
CREATE TABLE 
	anuncios(titulo VARCHAR(100),
			 duracion INT,
			 categoria VARCHAR(50),
			 clasificacion VARCHAR(50),
			 sponsor VARCHAR(50),
			 id_Anuncios VARCHAR(10),
			 PRIMARY KEY (id_Anuncios),
			 FOREIGN KEY (sponsor) REFERENCES sponsor(id_sponsor));-- UPDATE ON CASCADE;

CREATE TABLE 
	usuarios(usuario VARCHAR (20),
	 		 password VARCHAR (25),
			 email VARCHAR(30),
	 		 tipo_suscripcion VARCHAR (15),
	 		 activo_desde DATE,
			  PRIMARY KEY(usuario));--

CREATE TABLE 
	perfiles(id_perfil VARCHAR (10),
	 		 nombre_perfil VARCHAR(20),
	 		 tipo_perfil VARCHAR (10),
	 		 usuario VARCHAR (20),
			 PRIMARY KEY (id_perfil),
			 FOREIGN KEY(usuario) REFERENCES usuarios(usuario));

CREATE TABLE favoritos(id_perfil VARCHAR(50),
					  fecha_add DATE,
					  id_pelicula VARCHAR(10),
					  PRIMARY KEY(id_perfil, fecha_add, id_pelicula),
					  FOREIGN KEY(id_pelicula) REFERENCES peliculas(id_pelicula),
				   	  FOREIGN KEY(id_perfil) REFERENCES perfiles(id_perfil));
	

CREATE TABLE premios(
	id_premio VARCHAR(10),
	nominacion VARCHAR(10),
	ceremonia VARCHAR(15),
	anio VARCHAR(4),
	categoria VARCHAR(15),
	PRIMARY KEY(id_premio)
);

CREATE TABLES generos(
	genero VARCHAR(20),
	descripcion VARCHAR(50),
	PRIMARY KEY(genero)
);

ALTER TABLE peliculas
ADD FOREIGN KEY(director) REFERENCES director(nombre)

CREATE TABLE recomendados(id_pelicula VARCHAR(10))
--Relaciones--	 


CREATE TABLE 
	pelicula_actor(id_pelicula VARCHAR(10),
				   id_actor VARCHAR(10),
				   FOREIGN KEY(id_pelicula) REFERENCES peliculas(id_pelicula),
				   FOREIGN KEY(id_actor) REFERENCES actores(id_actor),
				   PRIMARY KEY (id_pelicula, id_actor));
				   
CREATE TABLE 
	pelicula_director(id_pelicula VARCHAR(10),
				   	  id_director VARCHAR(10),
				   	  FOREIGN KEY(id_pelicula) REFERENCES peliculas(id_pelicula),
				   	  FOREIGN KEY(id_director) REFERENCES director(id_director),
				   	  PRIMARY KEY (id_pelicula, id_director));
					  
CREATE TABLE 
	productora_pelicula(id_pelicula VARCHAR(10),
				   	    nombre VARCHAR(10),
				   	    FOREIGN KEY(id_pelicula) REFERENCES peliculas(id_pelicula),
				   	    FOREIGN KEY(nombre) REFERENCES productora(nombre),
				   	    PRIMARY KEY (id_pelicula, nombre));
				
CREATE TABLE 
	reproduccion(id_Anuncios VARCHAR (10),
				 id_perfil VARCHAR(10),
				 id_pelicula VARCHAR(10),
				 fecha_reprod DATETIME,
				 hora_reprod TIME,
				 FOREIGN KEY (id_Anuncios) REFERENCES anuncios(id_Anuncios),
				 FOREIGN KEY (id_perfil) REFERENCES perfiles(id_perfil),
				 FOREIGN KEY (id_pelicula) REFERENCES peliculas(id_pelicula),
				 PRIMARY KEY (id_Anuncios, id_perfil, id_pelicula));

CREATE TABLE director_premio(id_premio VARCHAR(10),
							id_director VARCHAR(10),
							FOREIGN KEY(id_premio) REFERENCES premios(id_premio),
							FOREIGN KEY(id_director) REFERENCES director(id_director),
							PRIMARY KEY(id_premio, id_director)
							);

CREATE TABLE actor_premio(id_premio VARCHAR(10),
							id_actor VARCHAR(10),
							FOREIGN KEY(id_premio) REFERENCES premios(id_premio),
							FOREIGN KEY(id_actor) REFERENCES actores(id_actor),
							PRIMARY KEY(id_premio, id_actor)
							);

CREATE TABLE pelicula_premio(id_premio VARCHAR(10),
							id_pelicula VARCHAR(10),
							FOREIGN KEY(id_premio) REFERENCES premios(id_premio),
							FOREIGN KEY(id_pelicula) REFERENCES peliculas(id_pelicula),
							PRIMARY KEY(id_premio, id_pelicula)
							);

CREATE TABLE generos_peliculas(
	id_pelicula VARCHAR(10),
	genero VARCHAR(20),
	PRIMARY KEY(id_pelicula, genero)
);

-- INSERCIÓN DE DATOS A LAS TABLAS 
				 
INSERT INTO peliculas(duracion, id_pelicula, titulo, fecha_lanzamiento, genero, premios_ganados)
VALUES		(176, 'Q2ZLKBAJP0', 'The Batman', '2022/03/04', 'accion', '0')
INSERT INTO peliculas(duracion, id_pelicula, titulo, fecha_lanzamiento, genero, premios_ganados)
VALUES		(156, 'E04FBVZEDB', 'Dune', '2021/10/22', 'ficcion', '10')
INSERT INTO peliculas(duracion, id_pelicula, titulo, fecha_lanzamiento, genero, premios_ganados)
VALUES		(121, 'APPC1TUD6A', 'Crepúsculo', '2008/11/21', 'romance', '15')

INSERT INTO actores(nombre, edad, fecha_nac, pais_origen, nominaciones, premios, id_actores)
VALUES		('Robert Pattinson', 35, '1986/05/13', 'Inglaterra', '3', '0', '09JTUOY1OT')
INSERT INTO actores(nombre, edad, fecha_nac, pais_origen, nominaciones, premios, id_actores)
VALUES		('Timothee Chalamet', 26, '1995/12/27', 'Estados Unidos', '5', '2', 'OL6JKF5FXA')

INSERT INTO director(nombre, edad, fecha_nac, pais_origen, nominaciones, premios, id_director)
VALUES 		('Matt Reeves', '55', '1996/04/27', 'Estados Unidos', '2', '1', 'L7W6BN6UQY')

INSERT INTO productora(nombre, pais, presupuesto, c_empleados)
VALUES		('Warner Bros', 'Estados Unidos', 250000000, 250)
INSERT INTO productora(nombre, pais, presupuesto, c_empleados)
VALUES		('Legendary Pictures', 'Estados Unidos', 165000000, 210)

INSERT INTO sponsor(nombre, tipo_contrato, id_sponsor)
VALUES 		('Colgate','anual','WHZMLX829S')

INSERT INTO anuncios(titulo, duracion, categoria, clasificacion, sponsor, id_Anuncios)
VALUES 		('Lava tus dientes', '30', 'higiene', 'C', 'WHZMLX829S', 'Q6XY9R0LKB')

INSERT INTO perfiles(favoritos, nombre_perfil, tipo_perfil, usuario)
VALUES 		('The Batman', 'Elean', 'Adulto', 'premium')

INSERT INTO usuarios(usuario, password, tipo_suscripcion, activo_desde)
VALUES		('elean07', 'elean1234', 'premiun', '03/16/2022')

INSERT INTO pelicula_actor(id_pelicula, id_actores)
VALUES		('Q2ZLKBAJP0', '09JTUOY1OT')
INSERT INTO pelicula_actor(id_pelicula, id_actores)
VALUES		('APPC1TUD6A', '09JTUOY1OT')

INSERT INTO pelicula_director(id_pelicula, id_director)
VALUES		('Q2ZLKBAJP0', 'L7W6BN6UQY')

INSERT INTO productora_pelicula(id_pelicula, nombre)
VALUES		('Q2ZLKBAJP0', 'Warner Bros')

INSERT INTO reproduccion(id_anuncios, nombre_perfil, id_pelicula)
VALUES		('Q6XY9R0LKB', 'Elean', 'Q2ZLKBAJP0')

INSERT INTO peliculas VALUES(112"," 'w3r' ","'Interstellar' "," '2014-02-01' "," 'b' "," 'Christopher Nolan');



-- ¿Que fan ha observado más minutos de películas de un actor dado?

SELECT	
	u.usuario AS "Fan", 
	SUM(p.duracion) AS "Total observado"
FROM 	
	usuarios u,
	peliculas p,
	reproduccion r,
	pelicula_actor pa,
	actores a,
	perfiles pe
WHERE 
	r.nombre_perfil = pe.nombre_perfil AND 
	u.usuario = pe.usuario AND 
	pa.id_pelicula = p.id_pelicula AND 
	pa.id_actores = a.id_actores AND 
	r.id_pelicula = p.id_pelicula AND 
	a.nombre = 'Robert Pattinson'
GROUP BY 
	u.usuario
ORDER BY 
	"Total observado" DESC
LIMIT 1;


--Queries de reporte

--1

--2

--3

--4
SELECT tipo_suscripcion, COUNT(tipo_suscripcion)
FROM usuarios
WHERE tipo_suscripcion = 'Premium' AND activo_desde > NOW()::DATE - 180
GROUP BY tipo_suscripcion;

--5
SELECT hora_reprod, COUNT(hora_reprod) as hora
FROM reproduccion
WHERE fecha_reprod = '2022-04-18'
GROUP BY hora_reprod
ORDER by hora desc limit 1;

CREATE TABLE 
	peliculas(duracion INT,
			  id_pelicula VARCHAR(10),
			  titulo VARCHAR(100),
			  fecha_lanzamiento DATE,
			  genero VARCHAR(50),
			  premios_ganados INT,
			  PRIMARY KEY (id_pelicula))
		
CREATE TABLE 
	actores(nombre VARCHAR(50),
			edad INT,
			fecha_nac DATE,
			pais_origen VARCHAR(100),
			nominaciones INT,
			premios INT, 
			id_actores VARCHAR(10),
			PRIMARY KEY (id_actores))

CREATE TABLE 
	director(nombre VARCHAR(50),
			 edad INT,
			 fecha_nac DATE,
			 pais_origen VARCHAR(100),
			 nominaciones INT,
			 premios INT,
			 id_director VARCHAR(10),
			 PRIMARY KEY(id_director))
			 
CREATE TABLE 
	productora(nombre VARCHAR(50),
			   pais VARCHAR(100),
			   presupuesto FLOAT,
			   c_empleados INT,
			   PRIMARY KEY (nombre))
			   
CREATE TABLE 
	anuncios(titulo VARCHAR(100),
			 duracion INT,
			 categoria VARCHAR(50),
			 clasificacion VARCHAR(50),
			 sponsor VARCHAR(50),
			 id_Anuncios VARCHAR(10),
			 PRIMARY KEY (id_Anuncios))
		
CREATE TABLE 
	perfiles(favoritos VARCHAR (50),
	 		 nombre_perfil VARCHAR(50),
	 		 tipo_perfil VARCHAR (50),
	 		 usuario VARCHAR (50),
			 PRIMARY KEY (nombre_perfil))
			 
CREATE TABLE 
	usuarios(usuario VARCHAR (50),
	 		 password VARCHAR (50),
	 		 tipo_suscripcion VARCHAR (50),
	 		 activo_desde VARCHAR (50))
	
CREATE TABLE 
	sponsor(nombre VARCHAR(50),
		    tipo_contrato VARCHAR (50),
		    id_sponsor VARCHAR (10),
		    PRIMARY KEY (id_sponsor))

CREATE TABLE 
	pelicula_actor(id_pelicula VARCHAR(100),
				   id_actores VARCHAR(50),
				   FOREIGN KEY(id_pelicula) REFERENCES peliculas(id_pelicula),
				   FOREIGN KEY(id_actores) REFERENCES actores(id_actores),
				   PRIMARY KEY (id_pelicula, id_actores))
				   
CREATE TABLE 
	pelicula_director(id_pelicula VARCHAR(10),
				   	  id_director VARCHAR(10),
				   	  FOREIGN KEY(id_pelicula) REFERENCES peliculas(id_pelicula),
				   	  FOREIGN KEY(id_director) REFERENCES director(id_director),
				   	  PRIMARY KEY (id_pelicula, id_director))
					  
CREATE TABLE 
	productora_pelicula(id_pelicula VARCHAR(10),
				   	    nombre VARCHAR(50),
				   	    FOREIGN KEY(id_pelicula) REFERENCES peliculas(id_pelicula),
				   	    FOREIGN KEY(nombre) REFERENCES productora(nombre),
				   	    PRIMARY KEY (id_pelicula, nombre))
						
CREATE TABLE 
	reproduccion(id_Anuncios VARCHAR (10),
				 nombre_perfil VARCHAR(50),
				 id_pelicula VARCHAR(10),
				 FOREIGN KEY (id_Anuncios) REFERENCES anuncios(id_Anuncios),
				 FOREIGN KEY (nombre_perfil) REFERENCES perfiles(nombre_perfil),
				 FOREIGN KEY (id_pelicula) REFERENCES peliculas(id_pelicula),
				 PRIMARY KEY (id_Anuncios, nombre_perfil, id_pelicula))

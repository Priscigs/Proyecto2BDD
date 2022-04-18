#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 17 15:15:33 2022

@author: entropy
"""

import psycopg2

elementSearch = "Jujutsu Kaisen 0"

def searchByMovie(elementSearch):
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="FlygonXD12",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="proyecto2_1")
        cursor = connection.cursor()
        postgreSQL_select_Query = "select * from peliculas WHERE titulo like " + "\'" + elementSearch + "\'" 

        cursor.execute(postgreSQL_select_Query)
        print("Selecting rows from mobile table using cursor.fetchall")
        query = cursor.fetchall()
        
        print(query)
        if(query == None):
            print("No se han encontrado coincidencias")

        print("Print each row and it's columns values")
        for row in query:
            print(" ", row[2], )
            print("Duracion: ", row[0])
            print("Fecha de estreno: ", row[3])
            print("Director: ", row[5])
            print("Clasificación: ", row[4], "\n")
            
    except (Exception, psycopg2.Error) as error:
        print("Error while fetching data from PostgreSQL", error)

    finally:
        # closing database connection.
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")
            
def searchByActor(elementSearch):
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="FlygonXD12",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="proyecto2_1")
        cursor = connection.cursor()
        postgreSQL_select_Query = "SELECT nombre, id_actor FROM actores WHERE nombre = "+"\'"+ elementSearch +"\'";
        

        cursor.execute(postgreSQL_select_Query)
        print("Selecting rows from mobile table using cursor.fetchall")
        query = cursor.fetchall()
        
        if(query == None):
            print("No se han encontrado coincidencias")

        print("Print each row and it's columns values \n")
        for row in query:
            print("Actor: ", row[0], )
          
        postgreSQL_select_Query2 = "SELECT peliculas.titulo, peliculas.id_pelicula, pelicula_actor.id_pelicula, pelicula_actor.id_actor FROM peliculas, pelicula_actor WHERE peliculas.id_pelicula=pelicula_actor.id_pelicula AND pelicula_actor.id_actor= "+"\'"+ row[1] +"\'";
        
        cursor.execute(postgreSQL_select_Query2)
        query2 = cursor.fetchall()    
        if(query2 == None):
            print("No se han encontrado coincidencias")

        for row in query2:
            print("  ", row[0], )


    except (Exception, psycopg2.Error) as error:
        print("Error while fetching data from PostgreSQL", error)

    finally:
        # closing database connection.
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")
            
def searchByGenre(elementSearch):
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="FlygonXD12",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="proyecto2_1")
        cursor = connection.cursor()
        postgreSQL_select_Query = "SELECT peliculas.titulo, peliculas.id_pelicula, generos_peliculas.genero FROM peliculas, generos_peliculas WHERE peliculas.id_pelicula=generos_peliculas.id_pelicula AND generos_peliculas.genero=" + "\'" + elementSearch + "\'" 

        cursor.execute(postgreSQL_select_Query)
        print("Selecting rows from mobile table using cursor.fetchall")
        query = cursor.fetchall()
        
        if(query == None):
            print("No se han encontrado coincidencias")

        print("Print each row and it's columns values")
        for row in query:
            print(" ", row[0], )
            print("Género: ", row[2])

    except (Exception, psycopg2.Error) as error:
        print("Error while fetching data from PostgreSQL", error)

    finally:
        # closing database connection.
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")
            
def searchByDirector(elementSearch):
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="FlygonXD12",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="proyecto2_1")
        cursor = connection.cursor()
        postgreSQL_select_Query = "select * from peliculas WHERE director like " + "\'" + elementSearch + "\'" 

        cursor.execute(postgreSQL_select_Query)
        print("Selecting rows from mobile table using cursor.fetchall")
        query = cursor.fetchall()
        
        if(query == None):
            print("No se han encontrado coincidencias")

        print("Print each row and it's columns values")
        for row in query:
            print(" ", row[2], )
            print("Duracion: ", row[0])
            print("Fecha de estreno: ", row[3])
            print("Director: ", row[5])
            print("Clasificación: ", row[4], "\n")

    except (Exception, psycopg2.Error) as error:
        print("Error while fetching data from PostgreSQL", error)

    finally:
        # closing database connection.
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

            
searchByMovie("Jujutsu Kaisen 0")

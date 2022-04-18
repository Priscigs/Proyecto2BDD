#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 18 04:16:43 2022

@author: entropy
"""
import psycopg2

def deleteData(elementSearch, titulo):
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="FlygonXD12",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="proyecto2_1")
        cursor = connection.cursor()
        postgreSQL_select_Query = "Update peliculas set duracion = NULL, id_pelicula=NULL, titulo=NULL, fecha_lanzamiento=NULL, director=NULL, clasificacion=NULL where id_pelicula=" + "\'" + elementSearch + "\'" ;

        cursor.execute(postgreSQL_select_Query)
        print("Selecting rows from mobile table using cursor.fetchall")
        query = cursor.fetchall()
        
        if(query == None):
            print("No se han encontrado coincidencias")

        print("Se ha eliminado la pelicula: "+ titulo)

    except (Exception, psycopg2.Error) as error:
        print("Error while fetching data from PostgreSQL", error)

    finally:
        # closing database connection.
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")
            
def updateData(duracion, id_pelicula, titulo, fecha_lanzamiento, clasificacion, director):
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="FlygonXD12",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="proyecto2_1")
        cursor = connection.cursor()
        postgreSQL_select_Query = "Update peliculas set duracion =" + "\'" + duracion + "\'" +  ", titulo=" + "\'" + titulo + "\'" + ", fecha_lanzamiento=" + "\'" + fecha_lanzamiento + "\'" + ", director=" + "\'" + director + "\'" + ", clasificacion="+ "\'" + clasificacion + "\'" + " where id_pelicula=" + "\'" + id_pelicula + "\'" ;

        cursor.execute(postgreSQL_select_Query)
        print("Selecting rows from mobile table using cursor.fetchall")
        query = cursor.fetchall()
        
        if(query == None):
            print("No se han encontrado coincidencias")

        print("Se ha modificado la pelicula: "+ titulo)

    except (Exception, psycopg2.Error) as error:
        print("Error while fetching data from PostgreSQL", error)

    finally:
        # closing database connection.
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")
            
def insertData(duracion, id_pelicula, titulo, fecha_lanzamiento, clasificacion, director):
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="FlygonXD12",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="proyecto2_1")
        cursor = connection.cursor()
        postgreSQL_select_Query = "INSERT INTO peliculas VALUES(" + duracion +  ","  + "\'" + id_pelicula + "\'" + ","  + "\'" + titulo + "\'" + ","  + "\'" + fecha_lanzamiento + "\'" + ","  + "\'" + clasificacion + "\'" + ","  + "\'" + director + "\'" +")" ;

        cursor.execute(postgreSQL_select_Query)
        print("Selecting rows from mobile table using cursor.fetchall")
        query = cursor.fetchall()
        
        if(query == None):
            print("No se han encontrado coincidencias")

        print("Se ha añadido la película: "+ titulo)

    except (Exception, psycopg2.Error) as error:
        print("Error while fetching data from PostgreSQL", error)

    finally:
        # closing database connection.
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")
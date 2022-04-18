#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 18 12:45:32 2022

@author: entropy
"""
import psycopg2

def addFav(elementSearch):
   try:
       connection = psycopg2.connect(user="postgres",
                                     password="FlygonXD12",
                                     host="127.0.0.1",
                                     port="5432",
                                     database="proyecto2_1")
       cursor = connection.cursor()
       postgreSQL_select_Query = "SELECT peliculas.titulo, peliculas.id_pelicula, perfiles.id_perfil FROM peliculas, perfiles WHERE peliculas.id_pelicula = " + "\'" + elementSearch + "\'"; 

       cursor.execute(postgreSQL_select_Query)
       print("Selecting rows from mobile table using cursor.fetchall")
       query = cursor.fetchall()
       
       if(query == None):
           print("No se han encontrado coincidencias")

    
       
       insertQuery = "INSERT INTO favoritos VALUES(" + "\'" + query[0][2] + "\'" + ", " +"\'"+ query[0][1]+"\'" + ", DEFAULT)";
       print(query[0][0] + " Ha sido añadidad a la lista de favoritos")
       cursor.execute(insertQuery)
       

   except (Exception, psycopg2.Error) as error:
       print("Error while fetching data from PostgreSQL", error)

   finally:
       # closing database connection.
       if connection:
           cursor.close()
           connection.close()
           print("PostgreSQL connection is closed")

def showFav(elementSearch):
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="FlygonXD12",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="proyecto2_1")
        cursor = connection.cursor()
        postgreSQL_select_Query = "SELECT peliculas.titulo, peliculas.id_pelicula,perfiles.nombre_perfil, favoritos.id_pelicula, favoritos.id_perfil FROM peliculas, favoritos, perfiles WHERE favoritos.id_pelicula=peliculas.id_pelicula AND favoritos.id_perfil = " + "\'" + elementSearch + "\'"; 

        cursor.execute(postgreSQL_select_Query)
        print("Selecting rows from mobile table using cursor.fetchall")
        query = cursor.fetchall()
        
        if(query == None):
            print("No se han encontrado coincidencias")

        print(query[0][2])         

        for row in query:
            print(row[0])
            
        

    except (Exception, psycopg2.Error) as error:
        print("Error while fetching data from PostgreSQL", error)

    finally:
        # closing database connection.
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

addFav('sqd')
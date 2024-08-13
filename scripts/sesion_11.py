# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 17:05:28 2024

@author: Usuario
"""

import pandas as pd
import numpy as np

import os

## chdir: choose directory
os.chdir("C:/Users/Usuario/Documents/scidata/24_cdd_py/practicas/starwars")
starwars = pd.read_csv("starwars.csv")

#%%

starwars.head()
starwars.columns
starwars.shape

#%%
# Eliminar primera columna
starwars.drop("Unnamed: 0",axis=1,inplace = True)

#%%

### Selecciona las columnas name (nombre), height (estatura), 
### y gender (género).

subdata = starwars[["name","height","gender"]]

subdata.to_csv("mi_primer_csv.csv")

### Filtra los personajes que tienen una altura mayor a 180 cm

starwars[starwars["height"] > 180]

### Filtra los personajes que tienen una masa mayor a 50kg

starwars[starwars["mass"] > 50]

### Filtra los personajes que sí tienen estatura conocida

starwars[~starwars["height"].isna()]

### TAREA: Filtra los personajes que no tienen masa conocida

### TAREA: Filtra los personajes que son de género masculino

### Filtra los personajes que son de género femenino pero 
### no son humanos

condicion1 = starwars["gender"] == "feminine"  
condicion2 = starwars["species"] != "Human"

starwars[condicion1 & condicion2]
starwars[(starwars["gender"] == "feminine") & (starwars["species"] != "Human")]

### Filtra los personajes que son del planeta Tatooine o Naboo

condicion1 = starwars["homeworld"] == "Tatooine"  
condicion2 = starwars["homeworld"] == "Naboo"

starwars[condicion1 | condicion2]

################# Nota: Podemos aprovechar que se trata de la misma
################# columna en ambos en ambas condiciones y que dicha
################# columna es de tipo texto para mejorar el código

starwars[starwars["homeworld"].isin(["Tatooine","Naboo"])]

### Filtra los personajes que son del planeta Tatooine 
### o Naboo y cuyo peso sea mayor que el peso promedio de su 
### propio planeta

planetas_elegidos = starwars[starwars["homeworld"].isin(["Tatooine","Naboo"])]

planetas_elegidos

peso_naboo = planetas_elegidos[planetas_elegidos["homeworld"] == "Naboo"]["mass"].mean()
peso_tatooine = planetas_elegidos[planetas_elegidos["homeworld"] == "Tatooine"]["mass"].mean()

pesados_naboo = planetas_elegidos[(planetas_elegidos["homeworld"] == "Naboo") & (planetas_elegidos["mass"] > peso_naboo)]
pesados_tatooine = planetas_elegidos[(planetas_elegidos["homeworld"] == "Tatooine") & (planetas_elegidos["mass"] > peso_tatooine)]

pd.concat([pesados_naboo,pesados_tatooine],axis=0)


#### En realidad se resuelve así:
    
planetas_elegidos = starwars[starwars["homeworld"].isin(["Tatooine","Naboo"])]

pesos_promedio = planetas_elegidos.groupby("homeworld")["mass"].mean()

pesos_promedio["Naboo"]
pesos_promedio["Tatooine"]

condicion1 = (planetas_elegidos["homeworld"]=="Tatooine") &  (planetas_elegidos["mass"]>pesos_promedio["Tatooine"])
condicion2 = (planetas_elegidos["homeworld"]=="Naboo") &  (planetas_elegidos["mass"]>pesos_promedio["Naboo"])

planetas_elegidos[condicion1 | condicion2]

####### SESIÓN 11

#####################
#####################  EJERCICIO 2
#####################

starwars.columns

### Crea una nueva columna llamada imc que calcule la relación entre 
### masa y estarua de cada personaje (imc=10000*masa/estatura^2)

starwars["imc"] = 10000*starwars["mass"]/starwars["height"]**2

### TAREA: Crear una nueva columna que contenga las estaturas en metros

#####################
#####################  EJERCICIO 3
#####################

### Agrupa el dataset por la columna género y hogar y calcula el 
### promedio de la estatura para cada grupo.

starwars.groupby(["gender","homeworld"])["height"].mean()

starwars.groupby(["homeworld","gender"])["height"].mean()
    
### TAREA: lo mismo pero en lugar de planeta utilizar especie

### Agrupa por género y cuenta cuántas especies distintas
### hay en cada grupo.

starwars.groupby(["species","gender"]).size()  # n(_)  

### Resumir el DataFrame para mostrar el número total de personajes
### y la masa promedio para cada especie.

starwars.groupby("species").size()
starwars.groupby("species")["mass"].mean()

starwars.groupby("species").agg(total_elementos=("species","size"),
                                masa_promedio=("mass","mean"))

mis_resultados = pd.DataFrame({"Total":starwars.groupby("species").size(),
                              "masa_prom":starwars.groupby("species")["mass"].mean()})

#####################
#####################  EJERCICIO 4
#####################

### Ordena el DataFrame por la columna masa en orden descendente

starwars.sort_values(by="mass",ascending=False)

### Selecciona los cinco personajes con la mayor masa.

starwars.nlargest(5,"mass")

### Selecciona los cinco personajes con la menor masa.

starwars.nsmallest(5,"mass")

#####################
#####################  EJERCICIO 5
#####################

### Filtra los personajes cuyo color de cabello (hair_color) 
### contenga la palabra "auburn" (castaño).

starwars[starwars["hair_color"].str.contains("auburn",
                                             case=False,
                                             na=False)]

### Convierte todos los nombres (name) a mayúsculas.

starwars["name"] = starwars["name"].str.upper()

#####################
#####################  EJERCICIO 6
#####################

### Cuenta cuántos valores nulos hay en cada columna

starwars.isna().sum()

### Elimina las filas donde la columna mass tenga valores nulos.

starwars_masas = starwars[~starwars["mass"].isna()]

#####################
#####################  EJERCICIO 7
#####################

### TAREA: Filtra los personajes con estatura mayor al promedio de las 
### estaturas de todos los personajes y con masa es conocida; 
### agrupa por especie, y calcula el promedio de la masa para cada especie. 
### Finalmente, ordena los resultados por masa en orden ascendente.

## estat_prom = la estatura promedio de toda la tabla
## nva_tabla = tabla donde la estatura se conoce y además es mas grande que
##             estat_prom
## agrupa a nva_tabla por especie, fíjate en la columna masa y ahí calcula
## el valor promedio de la masa

### specie    peso_prom
### humanos       75
### mirialan      60
### wookie        99

## luego ordena respecto al peso promedio de manera ascendente

### specie    peso_prom
### mirialan      60
### humanos       75
### wookie        99


### TAREA: Para cada especie y género, haz un resumen de las estadísticas:
### estatura promedio, estatura máxima, estatura mínima, desviación de 
### la estatura y cuántos elementos tiene cada grupo especie-genero

#especie genero     estarua_prom estat_max, estat_min, sd_estat  total
#humano  femenino         x         x          x            x      9
#humano  masculin         x         x          x            x      26



    

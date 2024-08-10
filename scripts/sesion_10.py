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

### TAREA: Filtra los personajes que son del planeta Tatooine 
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















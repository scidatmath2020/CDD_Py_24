# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 14:58:55 2024

@author: Usuario
"""

import pandas as pd
import numpy as np
from siuba import *

import os

os.chdir("C:/Users/Usuario/Documents/scidata/24_cdd_py/practicas/poblacion_puebla")
puebla = pd.read_csv("ITER2020-Puebla.csv",
                       encoding="utf8")

#%%

### Seleccionar las columnas relevantes
### Columnas: municipio, nombre del municipio, localidad, nombre de la localidad, población total, viviendas totales

puebla_selec = puebla >> select(_.MUN, _.NOM_MUN, _.LOC, _.NOM_LOC,_.POBTOT,_.VIVTOT)

#### Filtrar los datos por un municipio específico
#### Por ejemplo, Atlixco

Atlixco = puebla_selec >> filter(_.NOM_MUN == "Atlixco")

#%%

### Agrupar los datos por municipio y calcular la población en cada uno

puebla_selec = puebla_selec >> mutate(CVE_MUN = _.MUN.astype(str) + "_" + _.NOM_MUN)

puebla_selec >> group_by(_.MUN) >> summarize(total_pobl = _.POBTOT.sum())


puebla_tot_mun = puebla_selec >> group_by(_.NOM_MUN) >> summarize(total_pobl = _.POBTOT.sum())

(puebla_selec >> 
    group_by(_.CVE_MUN) >> 
    summarize(total_pobl = _.POBTOT.sum()))

(puebla_selec >> 
    group_by(_.CVE_MUN) >> 
    summarize(total_pobl = _.POBTOT.sum()) >> 
    filter(_.CVE_MUN=="1_Acajete"))

#%%
### Ordenar los municipios por población total

puebla_tot_mun >> arrange(_.total_pobl)


#%%

## Calcular la proporción de la población total por municipio

puebla_tot_mun["total_pobl"].sum()

(
puebla_tot_mun >> mutate(prop = 100*_.total_pobl/puebla_tot_mun["total_pobl"].sum()) >>
    arrange(_.prop) 
)

#%%

### Filtrar municipios con más de 50,000 habitantes
puebla_tot_mun >> filter(_.total_pobl > 50000)

(puebla_tot_mun >> filter(_.total_pobl > 50000)).shape








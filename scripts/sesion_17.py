# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 17:04:54 2024

@author: Usuario
"""

import pandas as  pd
import numpy as np
from siuba import *
from plotnine import *
import os

os.chdir("C:\\Users\\Usuario\\Documents\\scidata\\24_cdd_py\\practicas\\automoviles")

mpg = pd.read_csv("mpg.csv")

#%%

mpg >> _.columns


mpg >> select(_.cty,_.hwy)


(
ggplot(data=mpg, mapping=aes(x="cty",y="hwy",color="displ",size="cyl")) +
    geom_point()
)

(
ggplot(data=mpg, mapping=aes(x="displ",y="cyl",color="class")) +
    geom_point()
)

(
mpg >> filter(_.cyl==8, _["class"] == "2seater") >>
    ggplot(mapping=aes(x="displ",y="cyl",color="class")) +
    geom_point(alpha=0.2)
)

(
ggplot(data=mpg, mapping=aes(x="class",y="hwy",alpha="cty")) +
    geom_point() 
)


( 
mpg >> filter((_["class"] == "compact") | (_["class"] == "subcompact")) >> 
ggplot(mapping=aes(x="cty",y="hwy",color="class")) +
    geom_point() +
    geom_abline(slope=1,intercept=0)
)


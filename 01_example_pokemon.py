# -*- coding: utf-8 -*-
"""
Created on Sun Apr 17 18:06:01 2022

@author: EDUARDO
"""

# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# For data handling
import numpy as np
import pandas as pd

print("hello")

# Pokemens are fun
# Pikachu is the best pokemon

# For visvalization
import matplotlib.pyplot as plt
import seaborn as sns

import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

v_path='C:/Users/EDUARDO/Desktop/01_PROYECTOS_BI/01_Python/01_datasets'
df=pd.read_csv(v_path+'/Pokemon.csv')
v1=df.head()
df.info()

import duckdb

v_db = duckdb.connect()
v_db.register("sql_poke", df)
v_r=v_db.execute("select * from sql_poke").fetchdf()

#v_db.execute("select  Type1 , count(*) from sql_poke group Type1 ")
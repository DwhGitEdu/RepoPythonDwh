# -*- coding: utf-8 -*-
"""
Created on Sun Apr 17 18:07:14 2022

@author: EDUARDO
"""

#%%

import pandas as pd
from sqlalchemy import text
from sqlalchemy import create_engine

query_gcp = """ 
             select * from gcp_bq_dwh_edu.tb_stg_dim_antiguedad 
             """

db = create_engine('bigquery://', 
                   credentials_path ="C:/Users/EDUARDO/Desktop/03_SCRIPTS/Sync/gcpdwhedu-d26bfaa72d49.json") 

df = pd.read_sql(query_gcp , con=db)
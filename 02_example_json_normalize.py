# -*- coding: utf-8 -*-
"""
Created on Sun Apr 17 18:06:40 2022

@author: EDUARDO
"""

#%%
import pandas as pd

data = [
{
 "squadName" : "Super Hero Squad", 
 "members" : 
     [
     {
     "id_time" :"20220101",         
     "id": "001",
     "company": "XYZ pvt ltd",
     "location": "London",
     "info": {
     "president": "Rakesh Kapoor",
     "contacts": {
                "email": "contact@xyz.com",
                 "tel": "9876543210"
                }
             },
              "employees": [
                           {"name": "A"},{"name": "B"},{"name": "C"}
                           ]
      },
      {
        "id_time" :"20220102",   
        "id": "002",
        "company": "PQR Associates",
        "location": "Abu Dhabi",
        "info": {
            "president": "Neelam Subramaniyam",
            "contacts": {
                    "email": "contact@pqr.com",
                    "tel": "8876443210"
             }
           },
        "employees": [
            {"name": "L"},{"name": "M"},{"name": "N"}
                     ]    
          
      },
      {
        "id_time" :"20220103",     
        "id": "003",
        "company": "PQz Associates",
        "info": {
            "president": "Neelam Subramaniyam",
            "contacts": {
                    "email": "contact@pqr.com"
                    
             }
           },
        "employees": [
            {"name": "X"},{"name": "W"},{"name": "Y"}
                     ]     
      },
      { 
        "id_time" :"20220104",     
        "id": "004",
        "company": "PQz Associates",
        "asociation": "Avenger",
        "info": {
            "president": "Neelam Subramaniyam",
            "contacts": {
                    "email": "contact@pqr.com"
                    
             }
           },
        "employees": [
            {"name": "A"},{"name": "B"},{"name": "C"}
                     ]     
      },
           {
     "id_time" :"20220301",         
     "id": "001",
     "asociation": "Avenger",
     "company": "XYZ pvt ltd",
     "location": "London",
     "info": {
     "president": "Rakesh Kapoor",
     "contacts": {
                "email": "contact@xyz.com",
                 "tel": "9876543210"
                }
             },
              "employees": [
                           {"name": "A"},{"name": "B"},{"name": "C"}
                           ]
      },
      {
        "id_time" :"20220314",   
        "id": "002",
        "asociation": "Avenger",
        "company": "PQR Associates",
        "location": "Abu Dhabi",
        "info": {
            "president": "Neelam Subramaniyam",
            "contacts": {
                    "email": "contact@pqr.com",
                    "tel": "8876443210"
             }
           },
        "employees": [
            {"name": "L"},{"name": "M"},{"name": "N"}
                     ]    
          
      },
      {
        "id_time" :"20220303",     
        "id": "003",
        "company": "PQz Associates",
        "info": {
            "president": "Neelam Subramaniyam",
            "contacts": {
                    "email": "contact@pqr.com"
                    
             }
           },
        "employees": [
            {"name": "X"},{"name": "W"},{"name": "Y"}
                     ]     
      },
      { 
        "id_time" :"20220315",     
        "id": "004",
        "company": "PQz Associates",
        "asociation": "Avenger",
        "info": {
            "president": "Neelam Subramaniyam",
            "contacts": {
                    "email": "contact@pqr.com"
                    
             }
           },
        "employees": [
            {"name": "A"},{"name": "B"},{"name": "C"}
                     ]     
      }
      
     
     ]
}  
]
    
    
df = pd.json_normalize(data , record_path=['members','employees'],
                       meta=['squadName' , 
                             ['members','id_time'] , 
                             ['members','id'] , 
                             ['members','company'] ,
                             ['members','asociation'] ,
                             ['members','location'],
                             ['members','info','president'],
                             ['members','info','contacts','email'],
                             ['members','info','contacts','tel'],
                             ] , errors='ignore')
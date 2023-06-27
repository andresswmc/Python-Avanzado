# -*- coding: utf-8 -*-
"""
Created on Fri Sep  9 11:00:13 2022

@author: Andres
"""
# Se importan las librerias a usar durante el desarrollo
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import hashlib
import glob
import os

## Se realiza la creación del nuevo Dataset para usuarios unicos mediante Hash
# Obtener el listado general de data a utilizar
os.listdir("C:/Users/Andres/Desktop/ProyectoDataEngineer/Datos")
df = os.path.join("C:/Users/Andres/Desktop/ProyectoDataEngineer/Datos", "*.csv")
listado_df = glob.glob(df)
dataframe = pd.concat(map(pd.read_csv, listado_df), ignore_index=True)

# Se crean dos nuevas columnas en el Dataframe
dataframe = dataframe.assign(tipo_numero_identificacion=None)
dataframe = dataframe.assign(hash=None)

# Se eliminan las columnas del dataframe original que no van a entrar dentro de las validaciones
dataframe = dataframe.drop(['id', 'nombre', 'apellido', 'email', 'genero', 'valor_tx'], axis=1)

# Se realiza la conversion de int a string de la columna numero_identificacion
dataframe["numero_identificacion"] = dataframe["numero_identificacion"].astype('object')

# Se unifica los valores de las columnas numero_identificacion y tipo_identificacion en la nueva columna tipo_numero_identificacion
dataframe["tipo_numero_identificacion"] = dataframe["tipo_identificacion"].map(str) + '' + dataframe["numero_identificacion"].map(str)

# Se procede a eliminar los registros duplicados del Dataframe utilizado
dataframe = dataframe.drop_duplicates()

# Crear hash o checksum para el dataframe utilizado hasta ahora
dataframe["hash"] = dataframe["tipo_numero_identificacion"].apply(hash)

## Se realiza la creación del nuevo Dataset para Transacciones mediante Hash

# Obtener el listado general de data a utilizar
os.listdir("C:/Users/Andres/Desktop/ProyectoDataEngineer/Datos")
df_tx = os.path.join("C:/Users/Andres/Desktop/ProyectoDataEngineer/Datos", "*.csv")
listado_df_tx = glob.glob(df_tx)
dataframe_tx = pd.concat(map(pd.read_csv, listado_df_tx), ignore_index=True)

# Se crean dos nuevas columnas en el Dataframe
dataframe_tx = dataframe_tx.assign(hash=None)

# Se eliminan las columnas del dataframe original que no van a entrar dentro de las validaciones
dataframe_tx = dataframe_tx.drop(['numero_identificacion', 'tipo_identificacion', 'id', 'email', 'genero'], axis=1)

# Crear hash o checksum para el dataframe utilizado hasta ahora
dataframe_tx["hash"] = dataframe_tx["valor_tx"].apply(hash)

# Se procede a eliminar los registros duplicados del Dataframe utilizado
dataframe_tx = dataframe_tx.drop_duplicates()

# Por ultimo se imprime el hash de las primeras lineas del dataframe de Transacciones
dataframe_tx["hash"].head(10)

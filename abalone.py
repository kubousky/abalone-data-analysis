import numpy as np
import pandas as pd
import datapackage

data_url = 'https://datahub.io/machine-learning/abalone/datapackage.json'


# to load Data Package into storage
package = datapackage.Package(data_url)

# to load only tabular data
resources = package.resources
for resource in resources:
    if resource.tabular:
        df = pd.read_csv(resource.descriptor['path'])
        df.rename(columns={'Class_number_of_rings':'Rings'}, inplace=True)
# print(df.head())


""" reading data from a local file """

# list_nombres_columna = ['Sex','Length','Diameter','Height','Whole_weight','Shucked_weight','Viscera_weight','Shell_weight','Rings']
# df= pd.read_csv('abalone.data',names=list_nombres_columna)
# print(df.head())


""" 1) Establece los datatypes de cada columna """

df[['Rings']]=df[['Rings']].apply(pd.to_numeric)
df[['Length','Diameter','Height','Whole_weight','Shucked_weight','Viscera_weight']]=df[['Length','Diameter','Height','Whole_weight','Shucked_weight','Viscera_weight']].astype(float)
df[['Sex']]=df[['Sex']].astype(str)
# print(df.dtypes)

""" 2) Extrae la columna rings y ordénala crecientemente. """

df_rings = df['Rings']
df_rings.columns ='Rings'
df_rings = df_rings.sort_values()
# print(df_rings.head())

""" 3) Extrae la fila 15 y luego la posición (50,3) """

df_fila_15 = df.iloc[14]
# print(df_fila_15)


""" 4) Extrae las instancias que tienen más de 20 rings """

df_rings_mayor_20 = df[df['Rings'] > 20]
# print(df_rings_mayor_20)

""" 5) ¿Cuál es el rango de valores que toman los anillos? """

df_rings_max = df['Rings'].max()
# print(df_rings_max)
df_rings_min= df['Rings'].min()
# print(df_rings_min)


""" 6) ¿Cuántos sexos diferentes hay? """

df_sexo =df['Sex'].unique()
# print(len(df_sexo))
# print(df_sexo)


""" 7) ¿Cuántos valores faltantes hay? """

df.isnull()
# print(len(df))


""" 8) ¿Qué proporción de elementos hay de cada sexo? ¿Están equilibradas las cantidades? """

df_sexo=df[df['Sex'] == 'M']
df_sexo=df[df['Sex'] == 'F']
df_sexo=df[df['Sex'] == 'I']
# print (len(df_sexo))


""" 9) Agrupa por sexo y calcula las medias de todos los atributos """

df_sex = df.groupby(['Sex']).mean()
# print(df_sex)

""" 10) Selecciona las instancias que corresponden a conchas infantiles (I) """

df_shell = df[df['Sex']== 'I']
# print(df_shell)

""" 11) Selecciona las instancias que están entre 22 y 25 rings y que son males """

df_rings_males = df.loc[(df['Rings'] >= 22) & (df['Rings'] <= 25) & (df['Sex']=='M')] 
# print(df_rings_males)
#!/usr/bin/env python
# coding: utf-8

# In[34]:


import requests
from bs4 import BeautifulSoup
import os
import csv

# Hago la peticion para recuperar los datos que contine la url
url_analisis = 'https://www.codigospostales.com/'
peticion = requests.get(url_analisis)
# ecesito convertir la petición anterior en una estructura anidada para identificar la informacion de interés.
soup = BeautifulSoup(peticion.text, 'html.parser')
# Creo una lista con el codigo de provincia y descripcion que he localizado en "soup"
list_provincias = []
for soup.fieldset.li in soup.find_all('li'): # Bucle para leer todos los registros de interés para las siguientes operaciones.
    provincia = soup.fieldset.li.text  # Recupero cada texto que se encuentra en la estructura con etiquetas "fieldset"
                                       # seguidas de la etiqueta "li"
    list_provincias.append(provincia)  # Cada registro lo añado a la lista de provincias. 
# Cada elemento de la lista esta compuesto por un string que contiene el codigo de la provincia y su descripcion
# Voy a transformar cada elemento de "list_provincias" en una nueva lista compuesta por 2 elementos: codigo y descripción.
list_provincias2 = [element.split(' ') for element in list_provincias]
# Voy a crear un diccionario para poner como clave el codigo de la provincia y como valor la descripción.
provincias = {}
# Vamos a rellenar el diccionario con los valores que hay el la lista transformada "list_provincias2"
for i in range(len(list_provincias2)):
    x = list_provincias2[i]
    provincias[x[0]] = x[1]
print(provincias)
# Escribo el diccionario en un archivo csv.

currentDir = os.getcwd()
print(currentDir)
filename = 'Provincias.txt'
filePath = os.path.join(currentDir, filename)
print(filePath)
fichero = open(filePath)
fichero.close()


# In[ ]:





# In[ ]:





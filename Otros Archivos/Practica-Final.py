#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 12 11:39:52 2018

@author: frfdnpg
"""
import urllib2
import os
import requests
import csv
from bs4 import BeautifulSoup

url_analisis = 'https://www.codigospostales.com/'
peticion = requests.get(url_analisis)
soup = BeautifulSoup(peticion.text, 'html.parser')
print(soup.prettify())
for soup.fieldset.li in soup.find_all('li'):
    provincia = soup.fieldset.li.text
    
    print(provincia)



class Provincias():
    
    def __init__(seft):
        self.url = 'https://www.codigospostales.com/'
        self.cod_prov = 
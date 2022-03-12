import pygal
import json
from pycountry import countries
from pygal import style
from pygal.style import LightColorizedStyle, RotateStyle

with open("DataAnalysis\population_data.json") as file:
    data = json.load(file)

file.close()

for pais_dic in data:
    if pais_dic["Year"] == "2010":
        nombre_pais = pais_dic["Country Name"]
        poblacion = pais_dic["Value"]
        print(nombre_pais + ': ' + poblacion)

paises_diccionario = {}
for country in countries:
    codigo = country.alpha_2.lower()
    nombre = country.name
    for pais_dic in data:
        if nombre.lower() == pais_dic["Country Name"].lower():
            paises_diccionario[codigo] = int(float(pais_dic["Value"]))

paises1, paises2, paises3 = {}, {}, {}
for pais, poblacion in paises_diccionario.items():
    if poblacion < 10000000:
        paises1[pais] = poblacion
    elif poblacion >= 10000000 and poblacion < 100000000:
        paises2[pais] = poblacion
    else:
        paises3[pais] = poblacion

mp_style = RotateStyle('#CC3399', base_style=LightColorizedStyle)
mp = pygal.maps.world.World(style=mp_style)
mp.title = "Mapamundi"
mp.add ("2010, población < 10.000.000", paises1)
mp.add ("2010, 10.000.000 < población < 100.000.000", paises2)
mp.add ("2010, 100.000.000 < población", paises3)
mp.render_to_file('world_population.svg')


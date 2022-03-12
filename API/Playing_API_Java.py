import json
from pygal import style
import requests
import pygal
from pygal.style import LightColorizedStyle as LC, RotateStyle as RS

def printdic(dic):
    for keys, values in dic.items():
        print(str(keys) + ": " + str(values))


# Se obtienen los datos en un JavaScript Object Notation
url = "https://api.github.com/search/repositories?q=language:java&sort=stars"
file = requests.get(url)
print("Status code:", file.status_code)
source = file.json()

with open("API/datos.json", "w") as file:
    json.dump(source, file)

# Obtenemos los datos de "items"
nombre = []
estrellitas = []
for repo in source["items"]:
    nombre.append(repo["name"])
    estrella ={
        "value": repo["stargazers_count"], 
        "xlink": repo["html_url"], 
        "label": repo["description"] or "", 
    }
    estrellitas.append(estrella)

config = pygal.Config()
config.legend_at_bottom = True
config.x_labels = nombre
config.x_label_rotation = 45
config.rounded_bars = True

my_style = RS("#CC2244", base_style=LC)
diag = pygal.Bar(config=config, style=my_style)
diag.add('Repositorios de Java', estrellitas)
diag.render_to_file("Repositorios_Java.svg")







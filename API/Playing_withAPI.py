from pygal import colors
import requests
from datetime import datetime
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS, RotateStyle as PS

# Hacer una llamada a una API
url = "https://api.github.com/search/repositories?q=language:python&sort=stars"
source = requests.get(url)
print("Status code:", source.status_code)

# Guardar la llamada en un archivo json
response_dict = source.json()
print("Repositorios locales", response_dict["total_count"])

# Procesar resultados
print(response_dict.keys())

# Mostramos los resutados de los repositorios
print("Repositorios: ", len(response_dict["items"]))

# Examinar el primer repositorio
repo_dict0 = response_dict["items"][0]
# print(repo_dict0)
# print("\nnº Keys: ", len(repo_dict0))
# for key in repo_dict0.keys():
#     print(key)

print("Información del primer repositorio: ")
print("Nombre: ", repo_dict0["name"])
print("Propietario", repo_dict0["owner"]["login"])
print("URL: ", repo_dict0["owner"]["html_url"])
print("Stars", repo_dict0["stargazers_count"])
print("Fecha de creación", datetime.strptime(repo_dict0["created_at"].split("T")[0]+ " " + (repo_dict0["created_at"].split("T")[1]).split("Z")[0], "%Y-%m-%d %H:%M:%S") ) 
print("\n")

for repo in response_dict["items"]:
    print("Información de repositorios: ")
    print("Nombre: ", repo["name"])
    print("Propietario: ", repo["owner"]["login"])
    print("URL: ", repo["owner"]["html_url"])
    print("Stars: ", repo["stargazers_count"])
    print("Fecha de creación: ", datetime.strptime(repo["created_at"].split("T")[0]+ " " + (repo["created_at"].split("T")[1]).split("Z")[0], "%Y-%m-%d %H:%M:%S") ) 
    print("\n")

name, stars_plotdict = [], []
for repo in response_dict["items"]:
    name.append(repo["name"])
    plot_dict = {
        'value': repo['stargazers_count'],
        'label': repo['description'] or "",
        'xlink': repo['html_url'],
    }
    stars_plotdict.append(plot_dict)

# Visualización
config = pygal.Config()
config.show_legend = True
config.legend_box_size = 10
config.x_label_rotation = 45
config.title = "Repositorios mejor valorados"
config.show_y_guides = False

my_style = PS("#772244", base_style=LCS)
hist = pygal.Bar(config, style = my_style, x_label_rotation = 45, show_legend="True")
hist.add("Respositorios", stars_plotdict)
hist.x_labels = name
hist._title = "Repositorios mejor valorados"
hist.render_to_file("Repo_GH_Analysis.svg")
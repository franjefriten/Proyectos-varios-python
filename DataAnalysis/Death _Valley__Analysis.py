import csv
import numpy
import pygal
from datetime import datetime
from matplotlib import pyplot as plt

with open('DataAnalysis\death_valley_2014.csv') as file:
    source = csv.reader(file)
    cabecera = next(source)
    
    T_max, T_min, T_med = {}, {}, {}
    i = 0
    for linea in source:
        print(linea)
        T_max[datetime.strptime(linea[0], "%Y-%m-%d")] = linea[1]
        T_min[datetime.strptime(linea[0], "%Y-%m-%d")] = linea[3]
        T_med[datetime.strptime(linea[0], "%Y-%m-%d")] = linea[2]
        if i == 50: break
        else: i += 1
    

fig = plt.figure(num=1, dpi=160, figsize=(7, 5.5))
plt.scatter(T_max.keys(), T_max.values(), c='r', label="Temp Max (F)")
plt.scatter(T_med.keys(), T_med.values(), c='g', label="Temp Med (F)")
plt.scatter(T_min.keys(), T_min.values(), c='b', label="Temp Min (F)")
plt.legend()
plt.grid(True)
plt.show()

config = pygal.Config()
config.x_label_rotation = 45
config.legend_at_bottom_columns = True
config.y_title = "Temperaturas (F)"
config.x_title = "Fechas"

# graph = pygal.Bar(config=config, )
import csv
import matplotlib.pyplot as plt
from datetime import datetime

with open("DataAnalysis\sitka_weather_2018_full.csv") as file:
    lector = csv.reader(file)
    linea_Encabezado = next(lector)

    for indice, nombre_Dato in enumerate(linea_Encabezado):
        print(indice, nombre_Dato)

    temperaturaMax = []
    temperaturaMin = []
    temperaturaAvg = []
    fechas = []
    
    for fila in lector:
        try:
            temperaturaMax.append(int(fila[8])) 
            fechas.append(datetime.strptime(fila[2], "%Y-%m-%d") )
            temperaturaMin.append(int(fila[9])) 
        except:
            pass
 
    fig, ax = plt.subplots()
    plt.scatter(fechas[0:50], temperaturaMax[0:50], c='r', label="Temperatura Máxima")
    plt.scatter(fechas[0:50], temperaturaMin[0:50], c='b', label="Temperatura Mínima")
    ax.set_xticklabels(fechas[0:20], rotation=25, fontsize=12)
    ax.set_ylabel("Temperaturas (F)")
    ax.legend()
    plt.tick_params(axis='both', which='major', labelsize=9)
    plt.show()

    # Plot data
    fig = plt.figure(dpi=128, figsize=(10, 6))
    plt.plot(fechas, temperaturaMax, c='red', label="Temperatura Máxima")
    plt.plot(fechas, temperaturaMin, c='blue', label="Temperatura Mínima")
    # Format plot
    plt.title("Daily high temperatures, July 2014", fontsize=24)
    plt.xlabel('', fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel("Temperatura (F)", fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)
    plt.show()

file.close()
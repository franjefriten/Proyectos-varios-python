import pygal
import re
import csv
from pygal.style import RotateStyle, DarkColorizedStyle
from pygal import style


with open(r"covid-19-datos-de-casos-y-personas-fallecidas-por-grupo-de-edad-y-sexo-acumulados-desde-el-31-01.csv", "r") as file:
    source = csv.reader(file, delimiter=";")
    cabecera = next(source)
    casos_mujeres_07 = {"g0-9": 0, "g10-19": 0, "g20-29": 0, "g30-39": 0, \
        "g40-49": 0, "g50-59": 0, "g60-69": 0, "g70-79": 0, "g80-89": 0}
    casos_hombres_07 = {"g0-9": 0, "g10-19": 0, "g20-29": 0, "g30-39": 0, \
        "g40-49": 0, "g50-59": 0, "g60-69": 0, "g70-79": 0, "g80-89": 0}
    muertes_hombres = {"g0-9": 0, "g10-19": 0, "g20-29": 0, "g30-39": 0, \
        "g40-49": 0, "g50-59": 0, "g60-69": 0, "g70-79": 0, "g80-89": 0}
    muertes_mujeres = {"g0-9": 0, "g10-19": 0, "g20-29": 0, "g30-39": 0, \
        "g40-49": 0, "g50-59": 0, "g60-69": 0, "g70-79": 0, "g80-89": 0}
    iter = 0

    for linea in source:
        if re.match(" 202107\d+", linea[6]) and re.match("Dona / Mujer", linea[1]) and re.match("g0-9", linea[0]):
            iter += 1
            casos_mujeres_07["g0-9"] += int(linea[3])
            muertes_mujeres["g0-9"] += float(linea[4])
        if re.match(" 202107\d+", linea[6]) and re.match("Dona / Mujer", linea[1]) and re.match("g10-19", linea[0]):
            casos_mujeres_07["g10-19"] += int(linea[3])
            muertes_mujeres["g10-19"] += float(linea[4])
        if re.match(" 202107\d+", linea[6]) and re.match("Dona / Mujer", linea[1]) and re.match("g20-29", linea[0]):
            casos_mujeres_07["g20-29"] += int(linea[3])
            muertes_mujeres["g20-29"] += float(linea[4])
        if re.match(" 202107\d+", linea[6]) and re.match("Dona / Mujer", linea[1]) and re.match("g30-39", linea[0]):
            casos_mujeres_07["g30-39"] += int(linea[3])
            muertes_mujeres["g30-39"] += float(linea[4])
        if re.match(" 202107\d+", linea[6]) and re.match("Dona / Mujer", linea[1]) and re.match("g40-49", linea[0]):
            casos_mujeres_07["g40-49"] += int(linea[3])
            muertes_mujeres["g40-49"] += float(linea[4])
        if re.match(" 202107\d+", linea[6]) and re.match("Dona / Mujer", linea[1]) and re.match("g50-59", linea[0]):
            casos_mujeres_07["g50-59"] += int(linea[3])
            muertes_mujeres["g50-59"] += float(linea[4])
        if re.match(" 202107\d+", linea[6]) and re.match("Dona / Mujer", linea[1]) and re.match("g60-69", linea[0]):
            casos_mujeres_07["g60-69"] += int(linea[3])
            muertes_mujeres["g60-69"] += float(linea[4])
        if re.match(" 202107\d+", linea[6]) and re.match("Dona / Mujer", linea[1]) and re.match("g70-79", linea[0]):
            casos_mujeres_07["g70-79"] += int(linea[3])
            muertes_mujeres["g70-79"] += float(linea[4])
        if re.match(" 202107\d+", linea[6]) and re.match("Dona / Mujer", linea[1]) and re.match("g80-89", linea[0]):
            casos_mujeres_07["g80-89"] += int(linea[3])
            muertes_mujeres["g80-89"] += float(linea[4])


        if re.match(" 202107\d+", linea[6]) and re.match("Home / Hombre", linea[1]) and re.match("g0-9", linea[0]):
            casos_hombres_07["g0-9"] += int(linea[3])
            muertes_hombres["g0-9"] += float(linea[4])
        if re.match(" 202107\d+", linea[6]) and re.match("Home / Hombre", linea[1]) and re.match("g10-19", linea[0]):
            casos_hombres_07["g10-19"] += int(linea[3])
            muertes_hombres["g10-19"] += float(linea[4])
        if re.match(" 202107\d+", linea[6]) and re.match("Home / Hombre", linea[1]) and re.match("g20-29", linea[0]):
            casos_hombres_07["g20-29"] += int(linea[3])
            muertes_hombres["g20-29"] += float(linea[4])
        if re.match(" 202107\d+", linea[6]) and re.match("Home / Hombre", linea[1]) and re.match("g30-39", linea[0]):
            casos_hombres_07["g30-39"] += int(linea[3])
            muertes_hombres["g30-39"] += float(linea[4])
        if re.match(" 202107\d+", linea[6]) and re.match("Home / Hombre", linea[1]) and re.match("g40-49", linea[0]):
            casos_hombres_07["g40-49"] += int(linea[3])
            muertes_hombres["g40-49"] += float(linea[4])
        if re.match(" 202107\d+", linea[6]) and re.match("Home / Hombre", linea[1]) and re.match("g50-59", linea[0]):
            casos_hombres_07["g50-59"] += int(linea[3])
            muertes_hombres["g50-59"] += float(linea[4])
        if re.match(" 202107\d+", linea[6]) and re.match("Home / Hombre", linea[1]) and re.match("g60-69", linea[0]):
            casos_hombres_07["g60-69"] += int(linea[3])
            muertes_hombres["g60-69"] += float(linea[4])
        if re.match(" 202107\d+", linea[6]) and re.match("Home / Hombre", linea[1]) and re.match("g70-79", linea[0]):
            casos_hombres_07["g70-79"] += int(linea[3])
            muertes_hombres["g70-79"] += float(linea[4])
        if re.match(" 202107\d+", linea[6]) and re.match("Home / Hombre", linea[1]) and re.match("g80-89", linea[0]):
            casos_hombres_07["g80-89"] += int(linea[3])
            muertes_hombres["g80-89"] += float(linea[4])

iter = 100*iter
plot_hombres = []
plot_mujeres = []
for i in range(len(casos_hombres_07)):
    plot_hombres.append({"label": list(casos_hombres_07.keys())[i], "value": list(casos_hombres_07.values())[i]})
    plot_mujeres.append({"label": list(casos_mujeres_07.keys())[i], "value": list(casos_mujeres_07.values())[i]})

config = pygal.Config()
# configuración
config.show_legend = True
config.print_labels = True

# rueda = pygal.Pie(config=config, inner_radius=9)
# rueda.add("Hombres", plot_hombres)
# rueda.add(["Hombres " + str(grupo) for grupo in casos_hombres_07.keys()], list(casos_hombres_07.values()))
# rueda.add(["Mujeres " + str(grupo) for grupo in casos_mujeres_07.keys()], list(casos_mujeres_07.values()))
# rueda.add("Mujeres", plot_mujeres)
# rueda.title = "Casos de covid según el sexo y la edad"
# rueda.render_to_file("MujeresVsHombres.svg")


my_config = pygal.Config()
my_config.include_x_axis = True
my_config.x_label_rotation = 45

bars = pygal.StackedBar(config=my_config, width=200, height=150)







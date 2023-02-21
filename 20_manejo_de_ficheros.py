#### fichero .txt
import os

fichero = open("20_mi_archivo.txt", "w+")
#print(fichero.read())
#print(fichero.read(15))
#print(fichero.readline())
#print(fichero.readlines())
fichero.write("Esto sería un nuevo texto")
fichero.write("\n""Esto sería otro nuevo texto")
fichero.close()
os.remove("20_mi_archivo.txt")
fichero = open("20_un_nuevo_fichero.txt","w+")
fichero.write("Esta es la primera línea\nEsta es la segunda línea\nY por último, esta es la tercera línea")
fichero.close()

#### fichero j.son
import json

archivo_json = open("20_mi_archivo.json", "r+")
mi_diccionario = {
    "Nombre": "Darío",
    "Apellidos": "López Díaz",
    "NIF": "27.390.345J",
    "Teléfono": 623098734,
    "CP": 42229
}

json.dump(mi_diccionario, archivo_json, indent = 3)
archivo_json.close()

archivo_json = open("20_mi_archivo.json", "r+")


print("readline ", archivo_json.readline())
print("read(10)", archivo_json.read(10))
print("read()", archivo_json.read())
for elemento in archivo_json.readlines():
    print(elemento)

# fichero .csv

import csv

fichero_csv = open("20_mi_csv.csv","w+")

csv_editable = csv.writer(fichero_csv)
csv_editable.writerow(["Nombre", "Edad", "Puntos", "Aprobado"])
csv_editable.writerow(["Luís", "23", "4.5", "Suspenso"])
csv_editable.writerow(["Pedro", "18", "6", "Pasa"])
csv_editable.writerow(["María", "49", "9", "Pasa"])

fichero_csv.close()

# fichero .xlsx

#import xlrd

# fichero xml

import xml
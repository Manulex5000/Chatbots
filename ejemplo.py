import csv

# Crear un archivo CSV y escribir en él
with open("salida.csv", "w", newline="") as archivo:
    escritor = csv.writer(archivo)
    escritor.writerow(["Nombre", "Edad"])  # Escribir encabezados
    escritor.writerow(["Ana", 28])         # Escribir datos
    escritor.writerow(["Luis", 35])
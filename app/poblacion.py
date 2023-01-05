# Importamos la librería necesaria
import matplotlib.pyplot as plt
import csv

# Creamos una función para graficar
def generate_bar_chart(country, labels, values):
  fig, ax = plt.subplots()
  ax.bar(labels, values)
  plt.savefig(f'./imgs/{country}_poblacion.png')
  plt.close()

# Empezamos con la apertura del csv
path = './world_population.csv'
country = input('Ingresa el nombre de un Pais: ')

with open(path,'r') as csvfile:
    reader = csv.reader(csvfile,delimiter=',')
    header = next(reader)
    for row in reader:
      if row[2]==country:
        data = row

labels = header[5:13]
values = data[5:13]
generate_bar_chart(country, labels, values)
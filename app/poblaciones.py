# Importamos la librería necesaria
import matplotlib.pyplot as plt
import csv

# Creamos una función para generar una gráfica de pastel
def generate_pie_chart(continent, labels, values):
  fig, ax = plt.subplots()
  ax.pie(values, labels=labels)
  ax.axis('equal')
  plt.savefig(f'./imgs/{continent}_poblaciones.png')
  plt.close()

continent = input('Ingrese el nombre de un continente: ')

# Empezamos con la apertura del csv
path = './world_population.csv'
data = {}
with open(path,'r') as csvfile:
    reader = csv.reader(csvfile,delimiter=',')
    header = next(reader)
    for row in reader:
      if row[4] == continent:
        data[str(row[2])] = float(row[16])

generate_pie_chart(continent, data.keys(),data.values())
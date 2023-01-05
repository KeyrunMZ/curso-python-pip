import utils

data = [{'Country':'Colombia','Population':300}, {'Country':'Bolivia','Population':500}, {'Country':'Chile','Population':100}]

def run():
  keys, values = utils.get_population()
  print(f' keys = {keys} \n values = {values}')
  print( utils.population_by_country( data, 'Colombia'))

# ENTRY POINT(): Para diferenciar qué ejecutar cuando se llama como módulo y cuando se llama como script
if __name__ == '__main__':
  run()
# IMPORTAMOS LIBRERÍAS ----------------------

import random
import time

print("Esta es el proyecto de curso, Piedra, Papel o Tijera (V.2): \n")

print("🤖 Bienvenido al juego Piedra, Papel o tijera 🙋 \n")

# DEFINIMOS LAS FUNCIONES  ----------------------

  # El usuario debe seleccionar una opción
def user_options():
  aproval = False
  selection = input('Elije (Piedra, Papel o Tijera): ').capitalize()
  if(selection in opciones):
    aproval = True
  else:
    print("Debes elejir una de las opciones dadas!")
  return selection, aproval

  # Quien gana?
def ganador(user_selection, pc_selection):
  user_selection_number = opciones.index(user_selection)
  pc_selection_number = opciones.index(pc_selection)
  result = user_selection_number - pc_selection_number
  if result in (-2,1):
    print("USER GANA!")
    return (1,0)
  elif result in (-1,2):
    print("PC GANA!")
    return (0,1)
  else:
    print("EMPATE!")
    return (0,0)

# DEFINIMOS VARIABLES GLOBALES ----------------------

  # Declaramos las opciones
opciones = ('Piedra', 'Papel', 'Tijera')

  # Puntuación
puntosPc = 0
puntosUser = 0 

# CUERPO DEL PROGRAMA  ----------------------

  # Al mejor de cuantas?
repeticion = int(input("Al mejor de cuantas?: "))

for i in range(0,repeticion):
  print(f"\n\nROUND {i+1}:")
    # Computadora elija aleatoriamente Piedra, Papel o Tijeras.
  pc_selection = random.choice(opciones)

    # Ciclo de selección
  while True:
    user_selection, aproval = user_options()
    if aproval:
      break

    # Imprimimos las selecciones
  print(f"PC({pc_selection}) vs USER({user_selection})")

    # Asignamos los puntos a los ganadores
  puntos = ganador(user_selection,pc_selection)
  puntosUser+=puntos[0]
  puntosPc+=puntos[1]
  
  time.sleep(1)
  
    # Mostramos el marcador
  print(f"PC ({puntosPc}) - USER({puntosUser})")
  time.sleep(1)
  
    # En casos de que sea imposible remontar
  if(puntosPc > (repeticion-i)):
    break
  if(puntosUser > (repeticion-i)):
    break
  
print("\n\n")
if puntosPc == puntosUser:
  print("RESULTADO FINAL: EMPATE!")
elif puntosPc > puntosUser:
  print("RESULTADO FINAL: PC GANA!")
else:
  print("RESULTADO FINAL: USER GANA!")  
# Tablero de Juego
from tabulate import tabulate

# 1. Damos la bienvenida al usuario
def bienvenida_usuario():
  print("|BIENVENIDO A...|".center(65,'-'))
  print("""\n
██╗██████╗░███████╗░██████╗░█████╗░░█████╗░████████╗███████╗██╗
██║██╔══██╗██╔════╝██╔════╝██╔══██╗██╔══██╗╚══██╔══╝██╔════╝██║
██║██████╔╝█████╗░░╚█████╗░██║░░╚═╝███████║░░░██║░░░█████╗░░██║
╚═╝██╔══██╗██╔══╝░░░╚═══██╗██║░░██╗██╔══██║░░░██║░░░██╔══╝░░╚═╝
██╗██║░░██║███████╗██████╔╝╚█████╔╝██║░░██║░░░██║░░░███████╗██╗
╚═╝╚═╝░░╚═╝╚══════╝╚═════╝░░╚════╝░╚═╝░░╚═╝░░░╚═╝░░░╚══════╝╚═╝\n""")
  print("|Pulsa 1 para comenzar|".center(65, '-'))
  comenzar = input("")



# 2.1 Creamos el diseño del tablero

# Primero empezamos con las coordenadas
def coordenadas_tablero():
  tablero_juego_coordenadas = [
    ['0,0', '0,1', '0,2', '0,3', '0,4', '0,5', '0,6', '0,7', '0,8', '0,9'],
    ['1,0', '1,1', '1,2', '1,3', '1,4', '1,5', '1,6', '1,7', '1,8', '1,9'],
    ['2,0', '2,1', '2,2', '2,3', '2,4', '2,5', '2,6', '2,7', '2,8', '2,9'],
    ['3,0', '3,1', '3,2', '3,3', '3,4', '3,5', '3,6', '3,7', '3,8', '3,9'],
    ['4,0', '4,1', '4,2', '4,3', '4,4', '4,5', '4,6', '4,7', '4,8', '4,9'],
    ['5,0', '5,1', '5,2', '5,3', '5,4', '5,5', '5,6', '5,7', '5,8', '5,9'],
    ['6,0', '6,1', '6,2', '6,3', '6,4', '6,5', '6,6', '6,7', '6,8', '6,9'],
    ['7,0', '7,1', '7,2', '7,3', '7,4', '7,5', '7,6', '7,7', '7,8', '7,9']
  ]
  return tablero_juego_coordenadas



# 2,2 Definimos la estructura del tablero
def logica_tablero():
  tablero_juego_estructura = [
    ['▣', '▣', '▣', '▣', '▣', '▣', '▣', '▣', '▣', '▣'],
    ['▣', '--', '--', '--', '▣', '▣', '▣', '▣', '▣', '▣'],
    ['▣', '▣', '▣', '▣', '▣', '▣', '▣', '▣', '▣', '▣'],
    ['▣', '▣', '▣', '▣', '▣', '▣', '▣', '▣', '▣', '▣'],
    ['▣', '▣', '▣', '▣', '▣', '▣', '▣', '▣', '▣', '▣'],
    ['▣', '▣', '▣', '▣', '▣', '▣', '▣', '▣', '▣', '▣'],
    ['▣', '▣', '▣', '▣', '▣', '▣', '▣', '▣', '▣', '▣'],
    ['▣', '▣', '▣', '▣', '▣', '▣', '▣', '▣', '▣', '▣']
  ]
  
  return tablero_juego_estructura 

# 3, Preparacion del tablero
def preparacion_tablero(tablero_juego):
  # Según las instrucciones modificamos el tablero para poder iniciar la partida

  return tablero_juego

# 4, Mostramos el tablero
def imprimir_tablero(tablero):
  print(tabulate(tablero, tablefmt='plain'))


def main():
  # Empezamos la ejecución de nuestro código
  bienvenida_usuario()

  print("-".center(50, "-"))
  print("\nComencemos a jugar...\n\n")
  
  # Creamos el tablero de juego y lo mostramos al usuario
  print("Tablero de juego: ")
  tablero_juego = coordenadas_tablero()
  imprimir_tablero(tablero_juego)
  
  print('\n\n\n\n')
  tablero_visual = logica_tablero()
  imprimir_tablero(tablero_visual)
  # print("\n\n\n")

  # tablero_juego_preparado = preparacion_tablero(tablero_juego)

  # imprimir_tablero(tablero_juego_preparado)


main()


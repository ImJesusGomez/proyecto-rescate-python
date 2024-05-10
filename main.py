# Importamos la libreria tabulate que no ayuda a darle una estructura y orden a nuestro tablero
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


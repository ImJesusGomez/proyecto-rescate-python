# Importamos la libreria tabulate que no ayuda a darle una estructura y orden a nuestro tablero
from tabulate import tabulate
from tablero import coordenadas_tablero
from tablero import logica_tablero
from tablero import preparacion_tablero



# Creamos una función para dar la bienvenida al usuario
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



# Creamos una función que nos facilite mostrar al usuario el tablero de juego con la libreria tabulate
def imprimir_tablero(tablero):
  print(tabulate(tablero, tablefmt='plain'))


def main():
  # Empezamos la ejecución de nuestro código
  bienvenida_usuario()

  # Creamos las variables que usaremos a lo largo del proyecto
  tablero_coordenadas = coordenadas_tablero()
  tablero_estado_base = logica_tablero()
  jugadores = 0
  perder = False

  print("-".center(65, "-"))
  print("\nComencemos a jugar...\n\n")

  while(not perder):
    opcion = int(input("""\n\nMenú de Opciones: 
        1. Ver coordenadas del tablero
        2. Ver estado base del tablero
        3. Simbología del Tablero
        4. Agregar jugadores
        5. Jugar
        7. Rendirse\n\n"""))
    
    if(opcion == 1):
      print("\nCoordenadas del Tablero: \n")
      imprimir_tablero(tablero_coordenadas)
    elif(opcion == 2):
      print("\nEstado Base del Tablero: \n")
      imprimir_tablero(tablero_estado_base)
    elif(opcion == 3):
      print("""\nSimbología: 
          ||     # Pared vertical
          |      # Pared Vertical Medio Rota
          ▯      # Puerta Abierta
          ▮      # Puerta Cerrada
          ♟      # Jugador
          ⊡      # Casilla 
          --     # Pared Horizontal
          ﹣     # Pared Horizontal Medio Rota
          ✦      # Fuego
          ✧      # Humo
          ✆      # Punto de interes\n""")
    elif(opcion == 4):
      if(jugadores == 0):
        jugadores = int(input("\n¿Cuántos jugadores van a jugar?\n"))
        if(jugadores <= 0 or jugadores > 6):
          print("\nNúmero de jugadores no soportado. Mínimo 1 - Máximo 6\n")
          jugadores = 0
      elif(jugadores >= 1 or jugadores <= 6):
        print("\nYa no puede agregar más jugadores una vez la partida ha iniciado!!!\n")
    elif(opcion == 7):
      print("Ser bombero no es trabajo para todos. Hasta la próxima! ")
      break
  



if __name__ == '__main__':
  main()


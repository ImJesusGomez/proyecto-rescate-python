# Importamos la libreria tabulate que no ayuda a darle una estructura y orden a nuestro tablero
from tablero import coordenadas_tablero
from tablero import logica_tablero
from tablero import preparacion_tablero
from tablero import imprimir_tablero
import random



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
  print("|Pulsa start para comenzar|".center(65, '-'))
  comenzar = input("")


# Debido a la estructura de nuestro tablero, crear un dado de 6 y 8 caras no es una opción
# por lo que crearemos una función que simule el funcionamiento que tendria el lanzar los dados
def lanzar_dados():
  resultados_posibles = ['2.2', '2.3', '2.5', '2.7', '2.8', '2.10', '2.12', '2.14', '3.2', '3.3', '3.5', '3.7', '3.8', '3.10', '3.12',
                        '3.14', '5.2', '5.3', '5.5', '5.7', '5.8', '5.10', '5.12', '5.14', '6.2', '6.3', '6.5', '6.7', '6.8', '6.10', 
                        '6.12', '6.14', '8.2', '8.3', '8.5', '8.7', '8.8', '8.10', '8.12', '8.14', '9.2', '9.3', '9.5', '9.7', 
                        '9.8', '9.10', '9.12', '9.14']
  
  resultado = random.choice(resultados_posibles)
  i = resultado[0]
  i = int(i)
  j = resultado[2:]
  j = int(j)

  return resultado, i, j


def posicion_actual(tablero, jugador):
  # Recorremos las filas de la matriz
  for i, fila in enumerate(tablero):
    # Recorremos las columnas de la fila actual
    for j, valor in enumerate(fila):
      # Comparamos el valor actual con el elemento buscado
      if valor == jugador:
        # Si se encuentra el elemento, retornamos su ubicación
        return i, j
  
  return None


# Empezamos con la funcion que se encargará de ejecutar nuestro juego
def main():
  # Empezamos la ejecución de nuestro código
  bienvenida_usuario()

  # Creamos las variables que usaremos a lo largo del proyecto
  tablero_coordenadas = coordenadas_tablero()
  tablero_de_juego = preparacion_tablero()
  tablero_estado_base = logica_tablero()
  jugadores_visual = ['♚','♛', '♜', '♝', '♞', '♟']
  jugadores = 0
  perder = False
  turno = 0
  coordenada = ''
  casillas_iniciales = ['0.2', '0.3', '0.5', '0.7', '0.8', '0.10', '0.12', '0.14', '2.0', '3.0', '5.0', '6.0', '8.0', '9.0', '11.2', '11.3', '11.5', '11.7', '11.8', '11.8', '11.10', '11.12', '11.14', '2.16', '3.16', '5.16', '6.16', '8.16', '9.16']
  casilla_valida = True
  cubos_dmg = 0
  direccion = ''
  i = 0
  j = 0

  print("-".center(65, "-"))
  print("\nComencemos a jugar...\n\n")

  while(not perder):
    opcion = int(input("""\n\nMenú de Opciones: 
        1. Ver Coordenadas del Tablero
        2. Ver Estado Base del Tablero
        3. Simbología del Tablero
        4. Agregar jugadores
        5. Jugar a Rescate!
        6. Ver Estado Actual del Tablero
        7. Rendirse
        Elección: """))
    

    # Mostramos las coordenadas del tablero
    if(opcion == 1):
      print("\nCoordenadas del Tablero: \n")
      imprimir_tablero(tablero_coordenadas)
    # Mostramos el estado base del tablero sin preparaciones
    elif(opcion == 2):
      print("\nEstado Base del Tablero: \n")
      imprimir_tablero(tablero_estado_base)
    # Mostramos la simbología de los elementos de nuestro tablero
    elif(opcion == 3):
      print("""\nSimbología: 
          # Pared vertical                 ||
          # Pared Vertical Medio Rota      |
          # Puerta Abierta                 ▯
          # Puerta Cerrada                 ▮
          # Jugador                        ♚ ♛ ♜ ♝ ♞ ♟
          # Casilla                        ⊡
          # Pared Horizontal               --
          # Pared Horizontal Medio Rota    ﹣
          # Fuego                          ✦
          # Humo                           ✧
          # Punto de interes               ✆\n""")
    # Empezamos con la primera configuración del juego, agregar los jugadores
    elif(opcion == 4):
      continuar = True
      while(continuar):
          # Validamos que los jugadores ingresados sean válidos
          if(jugadores == 0):
            jugadores = int(input("\n¿Cuántos jugadores van a jugar?\n"))
            if(jugadores <= 0 or jugadores > 6):
              print("\nNúmero de jugadores no soportado. Mínimo 1 - Máximo 6\n")
              continuar = True
              jugadores = 0
            else:
              print("Jugadores Registrados...")
              continuar = False
          elif(jugadores >= 1 or jugadores <= 6):
            print("\nYa no puede agregar más jugadores una vez la partida ha iniciado!!!\n")
            continuar = False
    #Comenzamos con la ejecución principal de nuestro juego
    elif(opcion == 5):
      if(jugadores == 0): # Usamos un if para validar que el usuario ha ingresado anteriormente la cantidad de jugadores
        print("\n\nPara jugar debes primero indicar cuántos jugadores van a jugar!!!")
      else: 
        for jugador in range(jugadores):
          if(turno == 0): # Empezamos con el turno 0, en el cual el jugador deberá indicar donde posicionará su jugador
            while(casilla_valida): # Validamos que la casilla en la que inicio el jugador sea valida
              print("\nIndica las coordenadas de la casilla en la que deseas iniciar\nCasillas Disponibles:")
              for casilla in casillas_iniciales:
                print(casilla, end = ' ')
              coordenada = input("\nCoordenada: ")
              if coordenada in casillas_iniciales:
                i = int(coordenada[0])
                j = int(coordenada[2:])
                tablero_de_juego[i][j] = jugadores_visual[jugador]
                print('\nTablero de Juego: ')
                imprimir_tablero(tablero_de_juego)
                casilla_valida = False
              else:
                print("\nCasilla no válida")
                casilla = True
          else:
            i, j = posicion_actual(tablero_de_juego, jugadores_visual[jugador])
            print("Indica en qué direccion quieres moverte")
            direccion = input("Posición: ")

            if(direccion == "arriba"):
              tablero_de_juego[i-1][j] = jugadores_visual[jugador]
            elif(direccion == "izquierda"):
              tablero_de_juego[i][j-1] = jugadores_visual[jugador]
            elif(direccion == "derecha"):
              tablero_de_juego[i][j+1] = jugadores_visual[jugador]
            elif(direccion == "abajo"):
              tablero_de_juego[i+1][j] = jugadores_visual[jugador]
        turno += 1
    # Mostramos el estado actual del tablero de juego
    elif(opcion == 6):
        print('\nTablero de Juego: ')
        imprimir_tablero(tablero_de_juego)
    elif(opcion == 7):
      print("\nSer bombero no es trabajo para todos. Hasta la próxima!!! ")
      break
  


if __name__ == '__main__':
  main()



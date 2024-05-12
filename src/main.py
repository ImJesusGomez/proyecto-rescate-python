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


# Empezamos con la funcion que se encargará de ejecutar nuestro juego
def main():
  # Empezamos la ejecución de nuestro código
  bienvenida_usuario()

  # Creamos las variables que usaremos a lo largo del proyecto
  tablero_coordenadas = coordenadas_tablero()
  tablero_estado_base = logica_tablero()
  tablero_de_juego = preparacion_tablero()
  jugadores = 0
  perder = False
  turno = 0
  jugadores_visual = ['♚','♛', '♜', '♝', '♞', '♟']

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
      if(jugadores == 0):
        print("\n\nPara jugar debes primero indicar cuántos jugadores van a jugar!!!")
      else:
        k = 0
        for jugador in range(jugadores):
          if(turno == 0):
            print('\nTablero de Juego: ')
            imprimir_tablero(tablero_de_juego)
            coordenada = input(("Indica las coordenadas de la casilla en la que deseas iniciar"))
            i = int(coordenada[0])
            j = int(coordenada[2:])
            tablero_de_juego[i][j] = jugadores_visual[k]
            k += 1
          else:
            pass
        turno += 1
    # Mostramos el estado actual del tablero de juego
    elif(opcion == 6):
        print('\nTablero de Juego: ')
        imprimir_tablero(tablero_de_juego)
    elif(opcion == 7):
      print("Ser bombero no es trabajo para todos. Hasta la próxima! ")
      break
  


if __name__ == '__main__':
  main()


